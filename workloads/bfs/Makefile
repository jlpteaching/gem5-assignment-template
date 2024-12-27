GEM5_ROOT ?= ../../gem5
CROSS_COMPILE=riscv64-linux-gnu-

all: bfs

clean:
	rm -f bfs bfs-asm

bfs: bfs.cpp
	$(CROSS_COMPILE)g++ bfs.cpp -o bfs -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum bfs

bfs-asm: bfs.cpp
	$(CROSS_COMPILE)g++ bfs.cpp -o bfs-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
