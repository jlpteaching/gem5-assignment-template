# Copyright (c) 2024 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.memory.memory import ChanneledMemory
from processors import HW2TimingSimpleCPU, HW2PipelinedCPU

HW2RISCVBoard = SimpleBoard

class HW2MESITwoLevelCache(MESITwoLevelCacheHierarchy):
    """
    HW2MESITwoLevelCache models a two-level cache hierarchy with MESI coherency
    protocol. The L1 cache is split into 64KiB of 8-way set associative
    instruction cache and 64KiB of 8-way set associative data cache. The L2
    cache is a unified 1MiB 4-way set associative cache.
    """
    def __init__(self):
        super().__init__(
            l1i_size="64KiB",
            l1i_assoc=8,
            l1d_size="64KiB",
            l1d_assoc=8,
            l2_size="256KiB",
            l2_assoc=4,
            num_l2_banks=4,
        )

class HW2DDR4(ChanneledMemory):
    """
    HW1DDR3_2400_8x8 models a 1 GiB single channel DDR4 DRAM memory with a data
    bus clocked at 2400MHz.
    """
    def __init__(self):
        super().__init__(DDR4_2400_8x8, 1, 128, size="1GiB")

__all__ = [
    "HW2RISCVBoard",
    "HW2MESITwoLevelCache",
    "HW2DDR4",
    "HW2TimingSimpleCPU",
    "HW2PipelinedCPU",
]
