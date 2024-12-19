# Copyright (c) 2024 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.simple_board import SimpleBoard
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)
from gem5.components.memory.dram_interfaces.ddr3 import DDR3_1600_8x8
from gem5.components.memory.dram_interfaces.ddr4 import DDR4_2400_8x8
from gem5.components.memory.dram_interfaces.lpddr5 import LPDDR5_6400_1x16_8B_BL32
from gem5.components.memory.memory import ChanneledMemory
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA

RISCVBoard = SimpleBoard
X86Board = SimpleBoard
ArmBoard = SimpleBoard

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

class DDR3(ChanneledMemory):
    """
    DDR3_1600_8x8 models a 1 GiB single channel DDR3 DRAM memory with a data
    bus clocked at 1600MHz. This model extends ChanneledMemory from gem5's
    standard library.
    """
    def __init__(self):
        super().__init__(
            dram_interface_class=DDR3_1600_8x8,
            num_channels=1,
            interleaving_size=128,
            size="1GiB",
        )


class DDR4(ChanneledMemory):
    """
    DDR3_2400_8x8 models a 1 GiB single channel DDR4 DRAM memory with a data
    bus clocked at 2400MHz.
    """
    def __init__(self):
        super().__init__(DDR4_2400_8x8, 1, 128, size="1GiB")


class LPDDR5(ChanneledMemory):
    """
    LPDDR5_6400_1x16_8B_BL32 models a 1 GiB 4 channel LPDDR5 DRAM memory with a
    data bus clocked at 6400MHz.

    The theoretical peak bandwidth of LPDDR5 is
    """
    def __init__(self):
        super().__init__(LPDDR5_6400_1x16_8B_BL32, 4, 128, size="1GiB")

class RISCVSingleCycleCPU(SimpleProcessor):
    """
    SingleCycleCPU models a single core CPU with support for the Arm
    instruction set architecture (ISA).
    CPUTypes.TIMING refers to TimingSimpleCPU which is an internal CPU model in
    gem5. This is a "single cycle" CPU model. Each instruction takes 0 cycles
    to execute (after fetch) except for memory instructions which are a
    variable number of cycles.
    """
    def __init__(self):
        super().__init__(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)

class ArmSingleCycleCPU(SimpleProcessor):
    """
    SingleCycleCPU models a single core CPU with support for the Arm
    instruction set architecture (ISA).
    CPUTypes.TIMING refers to TimingSimpleCPU which is an internal CPU model in
    gem5. This is a "single cycle" CPU model. Each instruction takes 0 cycles
    to execute (after fetch) except for memory instructions which are a
    variable number of cycles.
    """
    def __init__(self):
        super().__init__(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.ARM)

class X86SingleCycleCPU(SimpleProcessor):
    """
    SingleCycleCPU models a single core CPU with support for the x86
    instruction set architecture (ISA).
    CPUTypes.TIMING refers to TimingSimpleCPU which is an internal CPU model in
    gem5. This is a "single cycle" CPU model. Each instruction takes 0 cycles
    to execute (after fetch) except for memory instructions which are a
    variable number of cycles.
    """
    def __init__(self):
        super().__init__(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.X86)

__all__ = [
    "RISCVBoard",
    "X86Board",
    "ArmBoard",
    "MESITwoLevelCache",
    "DDR3",
    "DDR4",
    "LPDDR5",
    "RISCVSingleCycleCPU",
    "ArmSingleCycleCPU",
    "X86SingleCycleCPU",
]
