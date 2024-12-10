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

from gem5.utils.override import overrides
from gem5.components.boards.abstract_board import AbstractBoard
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)

# HW4MESICache models a two-level cache hierarchy with MESI coherency protocol.
# It allows for changing size of the L1D cache, its tag access latency and
# its data access latency. It is used as a base class for other caches
# that are going to be used for this assignment. All the cache models in this
# assignment, model a very fast L1I cache (tag and data access latencies of 1)
# with a capacity of 32 KiB. In addition, all the cache hierarchies have a
# 128 KiB L2 cache with a tag latency of 5 and a data latency of 6 cycles.


class HW4MESICache(MESITwoLevelCacheHierarchy):
    def __init__(self, l1d_size: str, l1_tag_lat: int, l1_data_lat: int):
        super().__init__(
            l1i_size="32 KiB",
            l1i_assoc=8,
            l1d_size=l1d_size,
            l1d_assoc=8,
            l2_size="32 KiB",
            l2_assoc=16,
            num_l2_banks=4,
        )
        self._l1_tag_lat = l1_tag_lat
        self._l1_data_lat = l1_data_lat

    def incorporate_cache(self, board: AbstractBoard):
        super().incorporate_cache(board)
        for controller in self._l1_controllers:
            controller.L1Dcache.tagAccessLatency = self._l1_tag_lat
            controller.L1Dcache.dataAccessLatency = self._l1_data_lat
        for controller in self._l2_controllers:
            controller.L2cache.tagAccessLatency = 5
            controller.L2cache.dataAccessLatency = 6


# HW4SmallCache extends HW4MESICache to set the following parameters for its
# L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 1


class HW4SmallCache(HW4MESICache):
    def __init__(self):
        super().__init__(l1d_size="16KiB", l1_tag_lat=1, l1_data_lat=1)


# HW4SmallCache extends HW4MESICache to set the following parameters for its
# L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 3


class HW4MediumCache(HW4MESICache):
    def __init__(self):
        super().__init__(l1d_size="32KiB", l1_tag_lat=1, l1_data_lat=3)


# HW4SmallCache extends HW4MESICache to set the following parameters for its
# L1D cache. size: 64 KiB, tag access latency: 3, data access latency: 3


class HW4LargeCache(HW4MESICache):
    def __init__(self):
        super().__init__(l1d_size="48KiB", l1_tag_lat=3, l1_data_lat=3)
