# Copyright (c) 2022 The Regents of the University of California
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met: redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer;
# redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution;
# neither the name of the copyright holders nor the names of its
# contributors may be used to endorse or promote products derived from
# this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import argparse

from gem5.simulate.simulator import Simulator

from components.processors import HW3BigCore, HW3LittleCore
from components.cache_hierarchies import HW3Cache
from components.memories import HW3DDR4
from components.boards import HW3RISCVBoard

from workloads.matmul_workload import MatMulWorkload
from workloads.bfs_workload import BFSWorkload
from workloads.bubble_sort_workload import BubbleSortWorkload
from workloads.roi_manager import exit_event_handler


def cpu_factory(size):
    if size == "little":
        return HW3LittleCore()
    elif size == "big":
        return HW3BigCore()
    else:
        raise ValueError(f"Size {size} not supported")

def workload_factory(workload_name):
    if workload_name == "matmul":
        return MatMulWorkload()
    elif workload_name == "bfs":
        return BFSWorkload()
    elif workload_name == "bubble":
        return BubbleSortWorkload()
    else:
        raise ValueError(f"Unknown workload name {workload_name}")

def get_inputs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "processor_size",
        type=str,
        help="Type of CPU to use.",
        choices=["big", "little"],
    )
    argparser.add_argument(
        "workload",
        type=str,
        help="Name of the microbenchmark to run.",
        choices=["matmul", "bfs", "bubble"],
    )
    args = argparser.parse_args()
    return args.processor_size, args.workload


if __name__ == "__m5_main__":
    size, workload = get_inputs()

    board = HW3RISCVBoard(
        clk_freq="4GHz",
        processor=cpu_factory(size),
        cache_hierarchy=HW3Cache(),
        memory=HW3DDR4(),
    )

    board.set_workload(workload_factory(workload))
    simulator = Simulator(
        board=board, full_system=False, on_exit_event=exit_event_handler
    )
    simulator.run()

    print("Finished simulation")
