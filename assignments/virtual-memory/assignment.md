---
Author: Jason Lowe-Power
Editor:
Title: Virtual Memory Translation Cache Designs
---

## Research question

*Should we allocate area to a TLB or to the page walk cache?*

*TODO*: Draw a picture of the system with how the page walk caches are connected.

### Useful stats

```text
simSeconds
```

The hits, misses, and total latency for the data TLB's (DTB) page walk cache.
You can divide the latency by the number of misses to get the average per miss latency (i.e., AMAT).
The latency is given in *ticks* not cycles or seconds.

```text
board.cache_hierarchy.dptw_caches.overallHits::total
board.cache_hierarchy.dptw_caches.overallMisses::total
board.cache_hierarchy.dptw_caches.overallMissLatency::total
```

The TLB stats (hits, misses, accesses).
Feel free to ignore the intruction TLB (itb).

```text
board.processor.switch.core.mmu.dtb.rdMisses
board.processor.switch.core.mmu.dtb.wrMisses
board.processor.switch.core.mmu.dtb.rdAccesses
board.processor.switch.core.mmu.dtb.wrAccesses
```

The accesses by the page table waker to memory and to the L2 cache

```text
board.memory.mem_ctrl.dram.bwTotal::processor.switch.core.mmu.dtb.walker
board.cache_hierarchy.l2-cache-0.overallAccesses::processor.switch.core.mmu.dtb.walker
board.cache_hierarchy.l2-cache-0.overallMisses::processor.switch.core.mmu.dtb.walker
board.cache_hierarchy.l2-cache-0.overallHits::processor.switch.core.mmu.dtb.walker
```
