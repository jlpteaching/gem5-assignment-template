# Copyright (c) 2021 The Regents of the University of California
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


from gem5.components.cachehierarchies.ruby.abstract_ruby_cache_hierarchy import AbstractRubyCacheHierarchy
from gem5.components.cachehierarchies.abstract_two_level_cache_hierarchy import AbstractTwoLevelCacheHierarchy
from gem5.coherence_protocol import CoherenceProtocol
from gem5.isas import ISA
from gem5.components.boards.abstract_board import AbstractBoard
from gem5.runtime import get_runtime_isa
from gem5.utils.requires import requires

from gem5.components.cachehierarchies.ruby.topologies.simple_pt2pt import SimplePt2Pt
from gem5.components.cachehierarchies.ruby.caches.mesi_two_level.l1_cache import L1Cache
from gem5.components.cachehierarchies.ruby.caches.mesi_two_level.l2_cache import L2Cache
from gem5.components.cachehierarchies.ruby.caches.mesi_two_level.directory import Directory
from gem5.components.cachehierarchies.ruby.caches.mesi_two_level.dma_controller import DMAController

from itertools import zip_longest
from m5.objects import SimpleNetwork, Switch, SimpleExtLink, SimpleIntLink

from m5.objects import (
    RubySystem,
    RubySequencer,
    DMASequencer,
    RubyPortProxy,
)


class HW5MESITwoLevelCacheHierarchy(
    AbstractRubyCacheHierarchy, AbstractTwoLevelCacheHierarchy
):
    """A two level private L1 shared L2 MESI hierarchy.

    In addition to the normal two level parameters, you can also change the
    number of L2 banks in this protocol.
    """

    def __init__(self, xbar_latency: int):
        AbstractRubyCacheHierarchy.__init__(self=self)
        AbstractTwoLevelCacheHierarchy.__init__(
            self,
            l1i_size="32KiB",
            l1i_assoc=8,
            l1d_size="32KiB",
            l1d_assoc=8,
            l2_size="512KiB",
            l2_assoc=8,
        )

        self._xbar_latency = xbar_latency

    def incorporate_cache(self, board: AbstractBoard) -> None:

        requires(coherence_protocol_required=CoherenceProtocol.MESI_TWO_LEVEL)

        cache_line_size = board.get_cache_line_size()

        self.ruby_system = RubySystem()

        # MESI_Two_Level needs 5 virtual networks
        self.ruby_system.number_of_virtual_networks = 5

        self.ruby_system.network = L1L2ClusterTree(self.ruby_system, self._xbar_latency)
        self.ruby_system.network.number_of_virtual_networks = 5

        self._num_l2_banks = len(board.get_processor().get_cores()) - 1

        self._l1_controllers = []
        for i, core in enumerate(board.get_processor().get_cores()):
            cache = L1Cache(
                self._l1i_size,
                self._l1i_assoc,
                self._l1d_size,
                self._l1d_assoc,
                self.ruby_system.network,
                core,
                self._num_l2_banks,
                cache_line_size,
                get_runtime_isa(),
                board.get_clock_domain(),
            )

            cache.sequencer = RubySequencer(
                version=i,
                dcache=cache.L1Dcache,
                clk_domain=cache.clk_domain,
            )

            if board.has_io_bus():
                cache.sequencer.connectIOPorts(board.get_io_bus())

            cache.ruby_system = self.ruby_system

            core.connect_icache(cache.sequencer.in_ports)
            core.connect_dcache(cache.sequencer.in_ports)

            core.connect_walker_ports(
                cache.sequencer.in_ports, cache.sequencer.in_ports
            )

            # Connect the interrupt ports
            if get_runtime_isa() == ISA.X86:
                int_req_port = cache.sequencer.interrupt_out_port
                int_resp_port = cache.sequencer.in_ports
                core.connect_interrupt(int_req_port, int_resp_port)
            else:
                core.connect_interrupt()

            self._l1_controllers.append(cache)

        self._l2_controllers = [
            L2Cache(
                self._l2_size,
                self._l2_assoc,
                self.ruby_system.network,
                self._num_l2_banks,
                cache_line_size,
            )
            for _ in range(self._num_l2_banks)
        ]
        # TODO: Make this prettier: The problem is not being able to proxy
        # the ruby system correctly
        for cache in self._l2_controllers:
            cache.ruby_system = self.ruby_system

        self._directory_controllers = [
            Directory(self.ruby_system.network, cache_line_size, range, port)
            for range, port in board.get_memory().get_mem_ports()
        ]
        # TODO: Make this prettier: The problem is not being able to proxy
        # the ruby system correctly
        for dir in self._directory_controllers:
            dir.ruby_system = self.ruby_system

        self._dma_controllers = []
        if board.has_dma_ports():
            dma_ports = board.get_dma_ports()
            for i, port in enumerate(dma_ports):
                ctrl = DMAController(self.ruby_system.network, cache_line_size)
                ctrl.dma_sequencer = DMASequencer(version=i, in_ports=port)
                self._dma_controllers.append(ctrl)
                ctrl.ruby_system = self.ruby_system

        self.ruby_system.num_of_sequencers = len(self._l1_controllers) + len(
            self._dma_controllers
        )
        self.ruby_system.l1_controllers = self._l1_controllers
        self.ruby_system.l2_controllers = self._l2_controllers
        self.ruby_system.directory_controllers = self._directory_controllers

        if len(self._dma_controllers) != 0:
            self.ruby_system.dma_controllers = self._dma_controllers

        # Create the network and connect the controllers.
        self.ruby_system.network.connectControllers(
            self._l1_controllers, self._l2_controllers, self._directory_controllers[0]
        )
        # self.ruby_system.network.connectControllers(
        #     self._l1_controllers + self._l2_controllers +self._directory_controllers
        # )
        self.ruby_system.network.setup_buffers()

        # Set up a proxy port for the system_port. Used for load binaries and
        # other functional-only things.
        self.ruby_system.sys_port_proxy = RubyPortProxy()
        board.connect_system_port(self.ruby_system.sys_port_proxy.in_ports)


from itertools import zip_longest
from m5.objects import SimpleNetwork, Switch, SimpleExtLink, SimpleIntLink


class L1L2ClusterTree(SimpleNetwork):
    """A simple tree network. This doesn't not use garnet.

    Assumptions:
      - The number of L1 controllers is the same as the number of L2
        controllers.
      - There is one directory

    Each L2 bank is paired with an L1 controller. The order of the controllers
    in the two lists determines the pairing.
    The L2s are connected to a single router (crossbar).
    The directory is then also connected to this router.
    """

    _intLinkId = 0
    _extLinkId = 0
    _routerId = 0

    @classmethod
    def _getIntLinkId(cls):
        cls._intLinkId += 1
        return cls._intLinkId - 1

    @classmethod
    def _getExtLinkId(cls):
        cls._extLinkId += 1
        return cls._extLinkId - 1

    @classmethod
    def _getRouterId(cls):
        cls._routerId += 1
        return cls._routerId - 1

    def __init__(self, ruby_system, xbar_latency):
        super().__init__()
        self.netifs = []
        self._xbar_latency = xbar_latency

        # TODO: These should be in a base class
        # https://gem5.atlassian.net/browse/GEM5-1039
        self.ruby_system = ruby_system

    def connectControllers(self, l1_ctrls, l2_ctrls, dir_ctrl):
        """Connect all of the controllers to routers and connect the routers
        together as specified in the docstring of the class.
        Assumptions:
        - The number of L1 controllers is the same as the number of L2
            controllers.
        - There is one directory
        """
        # NOTE: Hack for SE mode with a `- 1` here and the first two L1s
        # are connected to a single L2
        assert len(l1_ctrls) - 1 == len(l2_ctrls)

        routers = []
        int_links = []
        ext_links = []

        self.xbar = Switch(router_id = self._getRouterId())
        routers.append(self.xbar)

        # for every l1/l2 pair create a connection. Then, connect this to a
        # xbar.
        for i, (l1, l2) in enumerate(zip(l1_ctrls[1:], l2_ctrls)):
        # for i, (l1, l2) in enumerate(zip(l1_ctrls, l2_ctrls)):
            # Create the router/switch
            l1_switch = Switch(router_id=self._getRouterId())
            setattr(self, f"l1_switch_{i}", l1_switch)
            routers.append(getattr(self, f"l1_switch_{i}"))
            # Connect the l1
            setattr(
                self,
                f"l1_link_{i}",
                SimpleExtLink(
                    link_id=self._getExtLinkId(), ext_node=l1, int_node=l1_switch
                ),
            )
            ext_links.append(getattr(self, f"l1_link_{i}"))

            # Add router for L2
            l2_switch = Switch(router_id=self._getRouterId())
            setattr(self, f"l2_switch_{i}", l2_switch)
            routers.append(getattr(self, f"l2_switch_{i}"))
            # Connect the L2
            setattr(
                self,
                f"l2_link_{i}",
                SimpleExtLink(
                    link_id=self._getExtLinkId(), ext_node=l2, int_node=l2_switch
                ),
            )
            ext_links.append(getattr(self, f"l2_link_{i}"))

            # Connect L1 router to L2 router
            setattr(
                self,
                f"l1_l2_link{i}",
                SimpleIntLink(
                    link_id=self._getIntLinkId(),
                    src_node=l1_switch,
                    dst_node=l2_switch,
                ),
            )
            int_links.append(getattr(self, f"l1_l2_link{i}"))
            setattr(
                self,
                f"l2_l1_link{i}",
                SimpleIntLink(
                    link_id=self._getIntLinkId(),
                    src_node=l2_switch,
                    dst_node=l1_switch,
                ),
            )
            int_links.append(getattr(self, f"l2_l1_link{i}"))

            # Connect the L2 router to the xbar
            setattr(
                self,
                f"l2_xbar_link{i}",
                SimpleIntLink(
                    link_id=self._getIntLinkId(),
                    src_node=l2_switch,
                    dst_node=self.xbar,
                    latency=self._xbar_latency,
                ),
            )
            int_links.append(getattr(self, f"l2_xbar_link{i}"))
            setattr(
                self,
                f"xbar_l2_link{i}",
                SimpleIntLink(
                    link_id=self._getIntLinkId(),
                    src_node=self.xbar,
                    dst_node=l2_switch,
                    latency=self._xbar_latency,
                ),
            )
            int_links.append(getattr(self, f"xbar_l2_link{i}"))

        # Connect the directory to the xbar
        self.dir_ext_link = SimpleExtLink(
            link_id=self._getExtLinkId(), ext_node=dir_ctrl, int_node=self.xbar
        )
        ext_links.append(self.dir_ext_link)

        # HACK: Connect first L1 directory to the xbar
        self.hack_ext_link = SimpleExtLink(
            link_id=self._getExtLinkId(), ext_node=l1_ctrls[0], int_node=self.xbar
        )
        ext_links.append(self.hack_ext_link)

        self.ext_links = ext_links
        self.int_links = int_links
        self.routers = routers
