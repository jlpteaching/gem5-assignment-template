# Copyright (c) 2024 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.memory.memory import ChanneledMemory
from .processors import SingleCycleCPU, PipelinedCPU

RISCVBoard = SimpleBoard

class MESITwoLevelCache(MESITwoLevelCacheHierarchy):
    """
    MESITwoLevelCache models a two-level cache hierarchy with MESI coherency
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

class DDR4(ChanneledMemory):
    """
    DDR4 models a 1 GiB single channel DDR4 DRAM memory with a data
    bus clocked at 2400MHz.

    The theoretical peak bandwidth of DDR4 is 19.2 GB/s.
    """
    def __init__(self):
        super().__init__(DDR4_2400_8x8, 1, 128, size="1GiB")

__all__ = [
    "RISCVBoard",
    "MESITwoLevelCache",
    "DDR4",
    "SingleCycleCPU",
    "PipelinedCPU",
]
