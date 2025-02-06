"""

Usage
-----

```
gem5 run.py <workload_name> [--fs] [--tlb_entries entires] [--pwc_size large|small]
```
"""

from gem5.coherence_protocol import CoherenceProtocol
from gem5.components.boards.x86_board import X86Board
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_switchable_processor import (
    SimpleSwitchableProcessor,
)
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA
from gem5.resources.resource import obtain_resource, BinaryResource
from gem5.simulate.exit_event import ExitEvent
from gem5.simulate.simulator import Simulator
from gem5.utils.requires import requires
from components import SmallPWCHierarchy, LargePWCHierarchy

import m5
import argparse
from pathlib import Path

# This simulation requires using KVM with gem5 compiled for X86 simulation
# and with MESI_Two_Level cache coherence protocol.
requires(
    isa_required=ISA.X86,
    coherence_protocol_required=CoherenceProtocol.MESI_TWO_LEVEL,
    kvm_required=True,
)

parser = argparse.ArgumentParser(description="Run gem5 simulation")
parser.add_argument(
    "workload_name",
    choices=["bfs", "mm_block_ik"],
    help="The workload to run.",
)
parser.add_argument(
    "--fs",
    action="store_true",
    default=False,
    help="Run in full system (FS) mode. If not set, runs in syscall emulation (SE) mode.",
)
parser.add_argument(
    "--tlb_entries",
    type=int,
    default=16,
    help="The number of TLB entries to use.",
)
parser.add_argument(
    "--pwc_size",
    type=str,
    default="small",
    choices=["small", "large"],
    help="The size of the page walk cache.",
)
args = parser.parse_args()

workload_name = args.workload_name

# Use the new FlexiblePWC class
if args.pwc_size == "small":
    cache_hierarchy = SmallPWCHierarchy()
elif args.pwc_size == "large":
    cache_hierarchy = LargePWCHierarchy()
else:
    raise ValueError("Invalid pwc_size")

# Main memory
memory = SingleChannelDDR4_2400(size="3GiB")

# This is a switchable CPU. We first boot Ubuntu using KVM, then the guest
# will exit the simulation by calling "m5 exit" (see the `command` variable
# below, which contains the command to be run in the guest after booting).
# Upon exiting from the simulation, the Exit Event handler will switch the
# CPU type (see the ExitEvent.EXIT line below, which contains a map to
# a function to be called when an exit event happens).
if args.fs:
    processor = SimpleSwitchableProcessor(
        starting_core_type=CPUTypes.KVM,
        switch_core_type=CPUTypes.TIMING,
        isa=ISA.X86,
        num_cores=1,
    )
    for proc in processor.start:
        proc.core.usePerf = False
    processor._switchable_cores['switch'][0].core.mmu.dtb.size = args.tlb_entries
else:
    processor = SimpleProcessor(
        cpu_type=CPUTypes.TIMING,
        isa=ISA.X86,
        num_cores=1,
    )
    processor.cores[0].core.mmu.dtb.size = args.tlb_entries

board = X86Board(
    clk_freq="3GHz",
    processor=processor,
    memory=memory,
    cache_hierarchy=cache_hierarchy,
)

if args.fs:
    workload_fs = obtain_resource(f"{workload_name}_fs_run")
    board.set_workload(workload_fs)
    # Hack to get around readfile being a string and not a FileResource
    board.readfile = obtain_resource(
        f"{workload_name}-fs").get_local_path()
else:
    workload_se = obtain_resource(f"{workload_name}_x86_run")
    board.set_workload(workload_se)


def exit_event_handler():
    print("First exit: kernel booted")
    yield False  # gem5 is now executing systemd startup
    print("Second exit: Started `after_boot.sh` script")
    # The after_boot.sh script is executed after the kernel and systemd have
    # booted.
    yield False  # gem5 is now executing the `after_boot.sh` script

    print("Switching to Timing CPU")
    processor.switch()
    yield False  # gem5 is now executing the program. The application_command
                 # has an extra exit command to switch CPUs
                 # This is required since we're using the instruction version
                 # of the gem5 hypercalls.

    print("Third exit: Finished `after_boot.sh` script")
    # The after_boot.sh script will run a script if it is passed via
    # m5 readfile. This is the last exit event before the simulation exits.
    yield True  # End the simulation

def workbegin_handler():
    # Here we switch the CPU type to Timing.
    m5.stats.reset()
    print("reset stats at beginning of work")
    yield False

def workend_handler():
    print("At workend. Exiting")
    yield True  # End the simulation


simulator = Simulator(
    board=board,
    on_exit_event={
        # Here we want override the default behavior for the first m5 exit
        # exit event.
        ExitEvent.EXIT: exit_event_handler(),
        ExitEvent.WORKBEGIN: workbegin_handler(),
        ExitEvent.WORKEND: workend_handler(),
    },
    id=f"{'fs' if args.fs else 'se'}-{workload_name}-{args.tlb_entries}-{args.pwc_size}_pwc",
)
simulator.override_outdir(Path("m5out") / simulator.get_id())

simulator.run()

"""
gem5 -re run.py bfs --fs --pwc_size=small --tlb_entries 16 &
gem5 -re run.py bfs --fs --pwc_size=small --tlb_entries 32 &
gem5 -re run.py mm_block_ik --fs --pwc_size=small --tlb_entries 16 &
gem5 -re run.py mm_block_ik --fs --pwc_size=small --tlb_entries 32 &
gem5 -re run.py bfs --fs --pwc_size=large --tlb_entries 16 &
gem5 -re run.py bfs --fs --pwc_size=large --tlb_entries 32 &
gem5 -re run.py mm_block_ik --fs --pwc_size=large --tlb_entries 16 &
gem5 -re run.py mm_block_ik --fs --pwc_size=large --tlb_entries 32 &
gem5 -re run.py bfs &
gem5 -re run.py mm_block_ik &
"""
