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
from gem5.components.processors.base_cpu_core import BaseCPUCore
from gem5.components.processors.base_cpu_processor import BaseCPUProcessor

from m5.objects import RiscvO3CPU
from m5.objects.BranchPredictor import *

SimpleBranchPredictor = TournamentBP
LTAGEBranchPredictor = TAGE_SC_L_TAGE_64KB
PerceptronBranchPredictor = MultiperspectivePerceptron64KB
ComplexBranchPredictor = MultiperspectivePerceptronTAGE64KB


class HW3O3CPUCore(RiscvO3CPU):
    def __init__(
        self, width, rob_size, num_int_regs, num_fp_regs, branch_predictor_cls
    ):
        super().__init__()
        self.fetchWidth = width
        self.decodeWidth = width
        self.renameWidth = width
        self.issueWidth = width
        self.wbWidth = width
        self.commitWidth = width

        self.numROBEntries = rob_size

        self.numPhysIntRegs = num_int_regs
        self.numPhysFloatRegs = num_fp_regs

        self.branchPred = branch_predictor_cls()


class HW3O3CPUStdCore(BaseCPUCore):
    def __init__(
        self, width, rob_size, num_int_regs, num_fp_regs, branch_predictor_cls
    ):
        core = HW3O3CPUCore(
            width, rob_size, num_int_regs, num_fp_regs, branch_predictor_cls
        )
        super().__init__(core, ISA.RISCV)


class HW3O3CPU(BaseCPUProcessor):
    def __init__(
        self, width, rob_size, num_int_regs, num_fp_regs, branch_predictor_cls
    ):
        cores = [
            HW3O3CPUStdCore(
                width,
                rob_size,
                num_int_regs,
                num_fp_regs,
                branch_predictor_cls,
            )
        ]
        super().__init__(cores)

class HW3LittleCore(HW3O3CPU):
    def __init__(self):
        super().__init__(4, 256, 216, 208, ComplexBranchPredictor)

class HW3BigCore(HW3O3CPU):
    def __init__(self):
        super().__init__(8, 672, 352, 384, ComplexBranchPredictor)
