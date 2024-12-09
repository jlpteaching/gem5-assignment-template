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

# HW0TimingSimpleCPU models a single core CPU with support for the RISC-V
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


class HW0TimingSimpleCPU(SimpleProcessor):
    def __init__(self):
        super().__init__(cpu_type=CPUTypes.TIMING, num_cores=1, isa=ISA.RISCV)
