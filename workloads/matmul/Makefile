GEM5_ROOT ?= ../../gem5

all: mm mm-asm mm-gem5 mm-gem5-asm

clean:
	rm mm mm-asm mm-gem5 mm-gem5-asm

mm: mm.cpp
	riscv64-unknown-linux-gnu-g++ mm.cpp -o mm -static -O3

mm-asm: mm.cpp
	riscv64-unknown-linux-gnu-g++ mm.cpp -o mm-asm -static -O3 -S -fverbose-asm

mm-gem5: mm.cpp
	riscv64-unknown-linux-gnu-g++ mm.cpp -o mm-gem5 -static -O3 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5

mm-gem5-asm: mm.cpp
	riscv64-unknown-linux-gnu-g++ mm.cpp -o mm-gem5-asm -static -O3 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
