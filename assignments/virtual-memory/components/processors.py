# Copyright (c) 2025 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_switchable_processor import SimpleSwitchableProcessor
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.isas import ISA

def create_processor(fs_mode: bool, tlb_entries: int):
    """Create a processor based on the mode (FS or SE) and TLB entries.

    Args:
        fs_mode: If True, creates a switchable processor for FS mode
        tlb_entries: Number of TLB entries to configure

    Returns:
        A configured processor (either SimpleSwitchableProcessor or SimpleProcessor)
    """
    if fs_mode:
        processor = SimpleSwitchableProcessor(
            starting_core_type=CPUTypes.KVM,
            switch_core_type=CPUTypes.TIMING,
            isa=ISA.X86,
            num_cores=1,
        )
        for proc in processor.start:
            proc.core.usePerf = False
        processor._switchable_cores['switch'][0].core.mmu.dtb.size = tlb_entries
    else:
        processor = SimpleProcessor(
            cpu_type=CPUTypes.TIMING,
            isa=ISA.X86,
            num_cores=1,
        )
        processor.cores[0].core.mmu.dtb.size = tlb_entries

    return processor
