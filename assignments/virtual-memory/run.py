# Copyright (c) 2025 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

"""Main simulation script for virtual memory translation cache design exploration.

This script runs experiments to compare different virtual memory translation cache
designs, specifically analyzing the tradeoff between TLB size and page walk cache
configuration. It supports both full system (FS) and syscall emulation (SE) modes,
and allows configuration of:
- TLB entries: Number of TLB entries (e.g., 16, 32)
- Page walk cache size: Small or large configuration
- Workloads: Different memory-intensive benchmarks (bfs, mm_block_ik)

The script uses gem5's X86 board with a switchable processor that starts with KVM
(for fast boot in FS mode) and switches to detailed timing mode for the workload
execution. It collects statistics on TLB and page walk cache performance.

Usage
-----

```
gem5 run.py <workload_name> [--fs] [--tlb_entries entries] [--pwc_size large|small]
```
"""

from gem5.components.boards.x86_board import X86Board
from gem5.components.memory.single_channel import SingleChannelDDR4_2400
from gem5.resources.resource import obtain_resource
from gem5.simulate.exit_event import ExitEvent
from gem5.simulate.simulator import Simulator
from components import SmallPWCHierarchy, LargePWCHierarchy
from components.processors import create_processor

import m5
import argparse
from pathlib import Path

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

# Use create_processor since we need to do something weird for FS mode
processor = create_processor(fs_mode=args.fs, tlb_entries=args.tlb_entries)

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
    board.readfile = obtain_resource(f"{workload_name}-fs").get_local_path()
else:
    workload_se = obtain_resource(f"{workload_name}_x86_run")
    board.set_workload(workload_se)


# Note: this is only used in FS mode.
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

