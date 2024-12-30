from components import (
    RISCVBoard,
    MESITwoLevelCache,
    DDR4,
    OutOfOrderCPU,
)

from gem5.simulate.simulator import Simulator
from gem5.utils.multisim import multisim
from gem5.resources.resource import obtain_resource

multisim.set_num_processes(10)

def get_board(width, rob_size, num_int_regs, num_fp_regs):
    cache = MESITwoLevelCache()
    memory = DDR4()
    cpu = OutOfOrderCPU(width, rob_size, num_int_regs, num_fp_regs)

    board = RISCVBoard(
        clk_freq="1GHz", processor=cpu, cache_hierarchy=cache, memory=memory
    )

    return board

configurations = {
    "little": {"width": 4, "rob_size": 32, "num_int_regs": 64, "num_fp_regs": 64},
    "big": {"width": 12, "rob_size": 384, "num_int_regs": 512, "num_fp_regs": 512},
}

# for name, config in configurations.items():
#     board = get_board(**config)
#     print(f"Area of {name} configuration: {board.get_processor().get_area_score()}")
# exit(0)

for workload in obtain_resource("comparch-benchmarks"):
    for name in ["little", "big"]:
        config = configurations[name]
        board = get_board(**config)
        board.set_workload(workload)
        simulator = Simulator(board=board, id=f"{name}-{workload.get_id()}")
        multisim.add_simulator(simulator)
