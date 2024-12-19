GEM5_ROOT ?= ../../gem5

all: daxpy daxpy-gem5

clean:
	rm -f daxpy daxpy-asm daxpy-gem5 daxpy-gem5-asm

daxpy: daxpy.cpp
	riscv64-linux-gnu-g++ daxpy.cpp -o daxpy -static -O2
	md5sum daxpy

daxpy-asm: daxpy.cpp
	riscv64-linux-gnu-g++ daxpy.cpp -o daxpy-asm -static -O2 -S -fverbose-asm

daxpy-gem5: daxpy.cpp
	riscv64-linux-gnu-g++ daxpy.cpp -o daxpy-gem5 -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum daxpy-gem5

daxpy-gem5-asm: daxpy.cpp
	riscv64-linux-gnu-g++ daxpy.cpp -o daxpy-gem5-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
