GEM5_ROOT ?= ../../gem5
CROSS_COMPILE=riscv64-linux-gnu-

all: queens queens-asm queens-gem5 queens-gem5-asm

clean:
	rm queens queens-asm queens-gem5 queens-gem5-asm

queens: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens -static -O2

queens-asm: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens-asm -static -O2 -S -fverbose-asm

queens-gem5: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens-gem5 -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5

queens-gem5-asm: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens-gem5-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
