# Copyright (c) 2022 The Regents of the University of California
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.boards.abstract_board import AbstractBoard
from gem5.components.cachehierarchies.ruby.mesi_two_level_cache_hierarchy import (
    MESITwoLevelCacheHierarchy,
)


class TwoLevelCache(MESITwoLevelCacheHierarchy):
    """
    TwoLevelCache models a two-level cache hierarchy with MESI coherency
    protocol.
    It allows for changing size of the L1D cache, its tag access latency and
    its data access latency. It is used as a base class for other caches
    that are going to be used for this assignment. All the cache models in this
    assignment, model a very fast L1I cache (tag and data access latencies of
    1) with a capacity of 32 KiB. In addition, all the cache hierarchies have a
    128 KiB L2 cache with a tag latency of 5 and a data latency of 6 cycles.
    """

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


class SmallCache(TwoLevelCache):
    """
    SmallCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 1
    """

    def __init__(self):
        super().__init__(l1d_size="16KiB", l1_tag_lat=1, l1_data_lat=1)


class MediumCache(TwoLevelCache):
    """
    MediumCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 3
    """

    def __init__(self):
        super().__init__(l1d_size="32KiB", l1_tag_lat=1, l1_data_lat=3)


class LargeCache(TwoLevelCache):
    """
    LargeCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 3, data access latency: 3
    """

    def __init__(self):
        super().__init__(l1d_size="64KiB", l1_tag_lat=3, l1_data_lat=3)
