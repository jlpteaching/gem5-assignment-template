# Copyright (c) 2025 Jason Lowe-Power
# SPDX-License-Identifier: BSD-3-Clause

from gem5.components.cachehierarchies.classic.private_l1_private_l2_cache_hierarchy import (
    PrivateL1PrivateL2CacheHierarchy,
)
from gem5.components.boards.abstract_board import AbstractBoard
from gem5.components.cachehierarchies.classic.caches.mmu_cache import MMUCache

class PageWalkCacheHierarchy(PrivateL1PrivateL2CacheHierarchy):
    """
    A cache hierarchy with configurable page walk cache sizes that extends
    the PrivateL1PrivateL2CacheHierarchy
    """
    def __init__(
        self,
        l1d_size: str,
        l1i_size: str,
        l2_size: str,
        pwc_size: str = "8KiB"
    ) -> None:
        super().__init__(
            l1d_size=l1d_size,
            l1i_size=l1i_size,
            l2_size=l2_size,
        )
        self._pwc_size = pwc_size

    def incorporate_cache(self, board: AbstractBoard) -> None:
        # Then setup our custom-sized PTW caches
        self.iptw_caches = [
            MMUCache(size=self._pwc_size)
            for _ in range(board.get_processor().get_num_cores())
        ]
        self.dptw_caches = [
            MMUCache(size=self._pwc_size)
            for _ in range(board.get_processor().get_num_cores())
        ]

        super().incorporate_cache(board)

        # Connect the PTW caches to the L2 buses
        for i, _ in enumerate(board.get_processor().get_cores()):
            self.iptw_caches[i].mem_side = self.l2buses[i].cpu_side_ports
            self.dptw_caches[i].mem_side = self.l2buses[i].cpu_side_ports

    def _connect_table_walker(self, cpu_id: int, cpu) -> None:
        cpu.connect_walker_ports(
            self.iptw_caches[cpu_id].cpu_side,
            self.dptw_caches[cpu_id].cpu_side,
        )

class SmallPWCHierarchy(PageWalkCacheHierarchy):
    def __init__(self) -> None:
        super().__init__(
            l1d_size="32KiB",
            l1i_size="32KiB",
            l2_size="512KiB",
            pwc_size="1KiB"
        )

class LargePWCHierarchy(PageWalkCacheHierarchy):
    def __init__(self) -> None:
        super().__init__(
            l1d_size="32KiB",
            l1i_size="32KiB",
            l2_size="512KiB",
            pwc_size="16KiB"
        )

__all__ = [
    "SmallPWCHierarchy",
    "LargePWCHierarchy",
]
