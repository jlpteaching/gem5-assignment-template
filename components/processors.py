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

from m5.objects import *


# HW2TimingSimpleCPU models a single core CPU with support for the RISC-V
# instruction set architecture (ISA). This model extends SimpleProcessor class
# from gem5's standard librabry. Please refer to
#     gem5/src/python/gem5/components/processors/simple_processor.py
# for more documentation.
# Below is the function signature for the constructor of SimpleProcessor class.

# class SimpleProcessor(BaseCPUProcessor):
#     def __init__(
#         self, cpu_type: CPUTypes, num_cores: int, isa: Optional[ISA] = None
#     )

# CPUTypes.TIMING refers to TimingSimpleCPU which is an internal CPU model in
# gem5. Please refer to
#     https://www.gem5.org/documentation/general_docs/cpu_models/SimpleCPU
# to learn more about TimingSimpleCPU and other SimpleCPU models.


class HW2TimingSimpleCPU(SimpleProcessor):
    def __init__(self):
        super().__init__(CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)


# HW2FloatSIMDFU extend MinorDefaultFloatSimdFU.MinorDefaultFloatSimdFU is an
# internal gem5 model. Please refer to
#   gem5/src/cpu/minor/BaseMinorCPU.py
# for more information and documentation. HW2FloatSIMDFU implements a
# floating point and SIMD functional units for gem5's MinorCPU.
# MinorCPU is an internal gem5 model that models an in-order pipelined
# processor. Please refer to
#   https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
# to learn more about MinorCPU.


class HW2FloatSIMDFU(MinorDefaultFloatSimdFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        """
        :param operation_latency: number of cycles it takes to execute
        a floating point/SIMD instruction
        :param issue_latency: number of cycles it takes to decode and issue
        a floating point/SIMD instruction
        """
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency
        print(f"fp_op: {operation_latency}, fp_issue: {issue_latency}")


# HW2IntFU extend MinorDefaultIntFU.MinorDefaultIntFU is an internal gem5
# model. Please refer to
#   gem5/src/cpu/minor/BaseMinorCPU.py
# for more information and documentation. HW2IntFU implements an integer
# functional unit for gem5's MinorCPU. MinorCPU is an internal gem5 model that
# models an in-order pipelined processor. Please refer to
#   https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
# to learn more about MinorCPU.


class HW2IntFU(MinorDefaultIntFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        """
        :param operation_latency: number of cycles it takes to execute
        an integer instruction
        :param issue_latency: number of cycles it takes to decode and issue
        an integer instruction
        """
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency
        print(f"int_op: {operation_latency}, int_issue: {issue_latency}")


# HW2MinorFUPool extend MinorFUPool. MinorFUPool is an internal gem5
# model. Please refer to
#   gem5/src/cpu/minor/BaseMinorCPU.py
# for more information and documentation. HW2MinorFUPool implements a pool of
# functional units for gem5's MinorCPU. This pool includes two integer and one
# floating point and SIMD functional units.  MinorCPU is an internal gem5 model
# that models an in-order pipelined processor. Please refer to
#   https://www.gem5.org/documentation/general_docs/cpu_models/MinorCPU
# to learn more about MinorCPU.


class HW2MinorFUPool(MinorFUPool):
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


# HW2MinorCPUCore extends RiscvMinorCPU. It allows the user to modify certain
# pipeline latencies in certain functional units. Please refer to the class
# documentation below to understand the parameters better.
# RiscvMinorCPU is one of gem5's internal models for the MinorCPU.
# It implements MinorCPU for the RISC-V ISA.


class HW2MinorCPUCore(RiscvMinorCPU):
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


class HW2MinorCPU(BaseCPUProcessor):
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
