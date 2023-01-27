GEM5_ROOT ?= ../../gem5

all: bubble bubble-asm bubble-gem5 bubble-gem5-asm

clean:
	rm bubble bubble-asm bubble-gem5 bubble-gem5-asm

bubble: bubble.cpp
	riscv64-unknown-linux-gnu-g++ bubble.cpp -o bubble -static -O2

bubble-asm: bubble.cpp
	riscv64-unknown-linux-gnu-g++ bubble.cpp -o bubble-asm -static -O2 -S -fverbose-asm

bubble-gem5: bubble.cpp
	riscv64-unknown-linux-gnu-g++ bubble.cpp -o bubble-gem5 -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5

bubble-gem5-asm: bubble.cpp
	riscv64-unknown-linux-gnu-g++ bubble.cpp -o bubble-gem5-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
