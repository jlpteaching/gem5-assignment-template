# Copyright (c) 2022 The Regents of the University of California
# SPDX-License-Identifier: BSD-3-Clause

from gem5.isas import ISA
from gem5.components.processors.cpu_types import CPUTypes
from gem5.components.processors.simple_processor import SimpleProcessor
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor

from m5.objects import RiscvMinorCPU, MinorFUPool
from m5.objects import MinorDefaultIntFU, MinorDefaultIntMulFU
from m5.objects import MinorDefaultIntDivFU, MinorDefaultFloatSimdFU
from m5.objects import MinorDefaultMemFU, MinorDefaultFloatSimdFU
from m5.objects import MinorDefaultMiscFU


class HW2TimingSimpleCPU(SimpleProcessor):
    """
    HW2SingleCycleCPU models a single core CPU with support for the RISC-V
    instruction set architecture (ISA).
    CPUTypes.TIMING refers to TimingSimpleCPU which is an internal CPU model in
    gem5. This is a "single cycle" CPU model. Each instruction takes 0 cycles
    to execute (after fetch) except for memory instructions which are a
    variable number of cycles.
    """

    def __init__(self):
        super().__init__(CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)


class HW2FloatSIMDFU(MinorDefaultFloatSimdFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        """
        HW2FloatSIMDFU extend MinorDefaultFloatSimdFU.MinorDefaultFloatSimdFU
        is an internal gem5 model. Please refer to
        gem5/src/cpu/minor/BaseMinorCPU.py
        for more information and documentation. HW2FloatSIMDFU implements a
        floating point and SIMD functional units for gem5's MinorCPU.
        MinorCPU is an internal gem5 model that models an in-order pipelined
        processor. Please refer to
        https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
        to learn more about MinorCPU.

        :param operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        :param issue_latency: number of cycles it takes to decode and issue
        a floating point/SIMD instruction
        """
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency
        print(f"fp_op: {operation_latency}, fp_issue: {issue_latency}")



class HW2IntFU(MinorDefaultIntFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        """
        HW2IntFU extend MinorDefaultIntFU.MinorDefaultIntFU is an internal gem5
        model. Please refer to
        gem5/src/cpu/minor/BaseMinorCPU.py
        for more information and documentation. HW2IntFU implements an integer
        functional unit for gem5's MinorCPU. MinorCPU is an internal gem5 model that
        models an in-order pipelined processor. Please refer to
        https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
        to learn more about MinorCPU.

        :param operation_latency: number of cycles it takes to execute
        an integer instruction
        :param issue_latency: number of cycles it takes to decode and issue
        an integer instruction
        """
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency
        print(f"int_op: {operation_latency}, int_issue: {issue_latency}")


class HW2MinorFUPool(MinorFUPool):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
        """
        HW2MinorFUPool extend MinorFUPool. MinorFUPool is an internal gem5
        model. Please refer to
          gem5/src/cpu/minor/BaseMinorCPU.py
        for more information and documentation. HW2MinorFUPool implements a
        pool of functional units for gem5's MinorCPU. This pool includes two
        integer and one floating point and SIMD functional units.  MinorCPU is
        an internal gem5 model that models an in-order pipelined processor.
        Please refer to
          https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
        to learn more about MinorCPU.

        :param int_operation_latency: number of cycles it takes to execute
        an integer instruction
        :param int_issue_latency: number of cycles it takes to decode and issue
        an integer instruction
        :param fp_operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        :param fp_issue_latency: number of cycles it takes to decode and issue
        a floating point/SIMD instruction
        """
        super().__init__()
        self.funcUnits = [
            HW2IntFU(int_operation_latency, int_issue_latency),
            HW2IntFU(int_operation_latency, int_issue_latency),
            MinorDefaultIntMulFU(),
            MinorDefaultIntDivFU(),
            MinorDefaultMemFU(),
            MinorDefaultMiscFU(),
            HW2FloatSIMDFU(fp_operation_latency, fp_issue_latency),
        ]

class HW2MinorCPUCore(RiscvMinorCPU):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
        """
        HW2MinorCPUCore extends RiscvMinorCPU. It allows the user to modify
        pipeline latencies in certain functional units.
        RiscvMinorCPU is one of gem5's internal models for the MinorCPU.
        It implements MinorCPU for the RISC-V ISA.

        :param int_operation_latency: number of cycles it takes to execute
        an integer instruction
        :param int_issue_latency: number of cycles it takes to decode and issue
        an integer instruction
        :param fp_operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        :param fp_issue_latency: number of cycles it takes to decode and issue
        a floating point/SIMD instruction
        """
        super().__init__()
        self.executeFuncUnits = HW2MinorFUPool(
            int_operation_latency,
            int_issue_latency,
            fp_operation_latency,
            fp_issue_latency,
        )


# HW2MinorCPUStdCore extend BaseCPUCore. It wraps HW2MinorCPUCore into a gem5
# standard library core. Please refer to:
#   gem5/src/python/gem5/components/processors/base_cpu_core.py
# to learn more about BaseCPUCore.


class HW2MinorCPUStdCore(BaseCPUCore):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
        """
        :param int_operation_latency: number of cycles it takes to execute
        an integer instruction
        :param int_issue_latency: number of cycles it takes to decode and issue
        an integer instruction
        :param fp_operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        :param fp_issue_latency: number of cycles it takes to decode and issue
        a floating point/SIMD instruction
        """
        core = HW2MinorCPUCore(
            int_operation_latency,
            int_issue_latency,
            fp_operation_latency,
            fp_issue_latency,
        )
        super().__init__(core, ISA.RISCV)


# With the help of HWMinorCPUStdCore, HW2MinorCPU wraps MinorCPU into a
# BaseCPUProcessor. BaseCPUProcessor is one of gem5's internal models from the
# standard library. It allows the users to instantiate a MinorCPU for the
# RISC-V ISA with certain modifiable pipeline latencies. All the latencies are
# keyword (optional) arguments with default values. Please refer to
#   https://www.geeksforgeeks.org/keyword-and-positional-argument-in-python/
# to learn more about keyword and positional arguments in python.
# Lastly, please refer to the class documentation below to better understand
# what each argument means and how to use them to parameterize your models
# for your simulations.


class HW2PipelinedCPU(BaseCPUProcessor):
    def __init__(
        self,
        issue_latency: int = 2,
        int_operation_latency: int = 3,
        fp_operation_latency: int = 6,
    ):
        """
        :param issue_latency: number of cycles it takes to decode and issue
        an instruction
        :param int_operation_latency: number of cycles it takes to execute
        an integer instruction
        :param fp_operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        """
        cores = [
            HW2MinorCPUStdCore(
                int_operation_latency,
                issue_latency,
                fp_operation_latency,
                issue_latency,
            )
        ]
        super().__init__(cores)
