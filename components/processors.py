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

from m5.objects import MinorCPU, MinorFUPool
from m5.objects import MinorDefaultIntFU, MinorDefaultIntMulFU
from m5.objects import MinorDefaultIntDivFU, MinorDefaultFloatSimdFU
from m5.objects import MinorDefaultMemFU, MinorDefaultFloatSimdFU
from m5.objects import MinorDefaultMiscFU


class HW2TimingSimpleCPU(SimpleProcessor):
    def __init__(self):
        super().__init__(CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)


class HW2FloatSIMDFU(MinorDefaultFloatSimdFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency


class HW2IntFU(MinorDefaultIntFU):
    def __init__(self, operation_latency: int, issue_latency: int):
        super().__init__()
        self.opLat = operation_latency
        self.issueLat = issue_latency


class HW2MinorFUPool(MinorFUPool):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
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


class HW2MinorCPUCore(MinorCPU):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
        super().__init__()
        self.executeFuncUnits = HW2MinorFUPool(
            int_operation_latency,
            int_issue_latency,
            fp_operation_latency,
            fp_issue_latency,
        )


class HW2MinorCPUStdCore(BaseCPUCore):
    def __init__(
        self,
        int_operation_latency: int,
        int_issue_latency: int,
        fp_operation_latency: int,
        fp_issue_latency: int,
    ):
        core = HW2MinorCPUCore(
            int_operation_latency,
            int_issue_latency,
            fp_operation_latency,
            fp_issue_latency,
        )
        super().__init__(core, ISA.RISCV)


class HW2MinorCPU(BaseCPUProcessor):
    def __init__(
        self,
        int_operation_latency: int = 3,
        int_issue_latency: int = 1,
        fp_operation_latency: int = 6,
        fp_issue_latency: int = 1,
    ):
        cores = [
            HW2MinorCPUStdCore(
                int_operation_latency,
                int_issue_latency,
                fp_operation_latency,
                fp_issue_latency,
            )
        ]
        super().__init__(cores)
