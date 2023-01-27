GEM5_ROOT ?= ../../gem5

all: bfs bfs-asm bfs-gem5 bfs-gem5-asm

clean:
	rm bfs bfs-asm bfs-gem5 bfs-gem5-asm

bfs: bfs.cpp
	riscv64-unknown-linux-gnu-g++ bfs.cpp -o bfs -static -O2

bfs-asm: bfs.cpp
	riscv64-unknown-linux-gnu-g++ bfs.cpp -o bfs-asm -static -O2 -S -fverbose-asm

bfs-gem5: bfs.cpp
	riscv64-unknown-linux-gnu-g++ bfs.cpp -o bfs-gem5 -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5

bfs-gem5-asm: bfs.cpp
	riscv64-unknown-linux-gnu-g++ bfs.cpp -o bfs-gem5-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
