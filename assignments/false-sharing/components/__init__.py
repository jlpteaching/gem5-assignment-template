# Copyright (c) 2024 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.memory.memory import ChanneledMemory
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA

from .cache_hierarchies import MESITwoLevelCacheHierarchy

X86Board = SimpleBoard

class DDR4(ChanneledMemory):
    """
    DDR4 models a 1 GiB single channel DDR4 DRAM memory with a data
    bus clocked at 2400MHz.
    """

    def __init__(self):
        super().__init__(DDR4_2400_8x8, 1, 128, size="1GiB")


class O3CPU(SimpleProcessor):
    def __init__(self, num_cores: int):
        """
        O3CPU is an out of order processor with a configurable number of
        cores. Note that because of limitations of SE mode and OpenMP we need
        to have one more core than specified. E.g., for 4 threads you need 5
        cores. You should ignore the "first" core's stats.

        :param num_cores: Number of cores in the processor.
        """
        super().__init__(
            cpu_type=CPUTypes.O3, num_cores=num_cores + 1, isa=ISA.X86
        )

    def get_actual_num_cores(self):
        return len(self.cores) - 1


__all__ = [
    "X86Board",
    "DDR4",
    "O3CPU",
    "MESITwoLevelCacheHierarchy",
]
