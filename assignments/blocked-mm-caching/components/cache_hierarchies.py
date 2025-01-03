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
    """

    def __init__(self, l1d_size: str):
        super().__init__(
            l1i_size="32 KiB",
            l1i_assoc=8,
            l1d_size=l1d_size,
            l1d_assoc=8,
            l2_size="32 KiB",
            l2_assoc=16,
            num_l2_banks=4,
        )


class SmallCache(TwoLevelCache):
    """
    SmallCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 1
    """

    def __init__(self):
        super().__init__(l1d_size="16KiB")


class MediumCache(TwoLevelCache):
    """
    MediumCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 1, data access latency: 3
    """

    def __init__(self):
        super().__init__(l1d_size="32KiB")


class LargeCache(TwoLevelCache):
    """
    LargeCache extends TwoLevelCache to set the following parameters for its
    L1D cache. size: 64 KiB, tag access latency: 3, data access latency: 3
    """

    def __init__(self):
        super().__init__(l1d_size="64KiB")
