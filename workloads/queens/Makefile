GEM5_ROOT ?= ../../gem5
CROSS_COMPILE=riscv64-linux-gnu-

all: queens

clean:
	rm -f queens queens-asm

queens: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum queens

queens-asm: queens.cpp
	$(CROSS_COMPILE)g++ queens.cpp -o queens-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
