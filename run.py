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

from processors import TeachingMinorCPU, TeachingTimingSimpleCPU
from cache_hierarchies import TeachingMESITwoLevelCache
from memories import (
    TeachingDDR3_1600_8x8,
    TeachingDDR3_2133_8x8,
    TeachingLPDDR3_1600_1x32,
)
from boards import TeachingRISCVBoard
from workload import hello_workload, mm_workload

def cpu_factory(cpu_type):
    if cpu_type == "TimingSimpleCPU":
        return TeachingTimingSimpleCPU()
    elif cpu_type == "MinorCPU":
        return TeachingMinorCPU()
    else:
        raise ValueError(f"CPU Type {cpu_type} not supported")


def memory_factory(memory_type):
    if memory_type == "DDR3_1600_8x8":
        return TeachingDDR3_1600_8x8()
    elif memory_type == "DDR3_2133_8x8":
        return TeachingDDR3_2133_8x8()
    elif memory_type == "LPDDR3_1600_1x32":
        return TeachingLPDDR3_1600_1x32()
    else:
        raise ValueError(f"Memory Type {memory_type} not supported")


def get_inputs():
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
        "cpu_type",
        type=str,
        help="Type of CPU to use.",
        choices=["TimingSimpleCPU", "MinorCPU"],
    )
    argparser.add_argument(
        "cpu_freq", type=str, help="Frequency of the cpu clock."
    )
    argparser.add_argument(
        "memory_type",
        type=str,
        help="Type of the memory to use.",
        choices=["DDR3_1600_8x8", "DDR3_2133_8x8", "LPDDR3_1600_1x32"],
    )
    args = argparser.parse_args()
    return args.cpu_type, args.cpu_freq, args.memory_type


if __name__ == "__m5_main__":
    cpu_type, cpu_freq, memory_type = get_inputs()
    cpu = cpu_factory(cpu_type)
    cache = TeachingMESITwoLevelCache()
    memory = memory_factory(memory_type)
    board = TeachingRISCVBoard(
        clk_freq=cpu_freq, processor=cpu, cache_hierarchy=cache, memory=memory
    )

    board.set_se_binary_workload(hello_workload)
    simulator = Simulator(board=board, full_system=False)
    simulator.run()

    print(
        "Exiting @ tick {} because {}.".format(
            simulator.get_current_tick(),
            simulator.get_last_exit_event_cause(),
        )
    )
