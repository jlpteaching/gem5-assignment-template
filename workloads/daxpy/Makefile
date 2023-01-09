GEM5_ROOT ?= ../../gem5

all: daxpy daxpy-gem5

clean:
	rm daxpy daxpy-gem5

daxpy: daxpy.cpp
	riscv64-unknown-linux-gnu-g++ -o daxpy daxpy.cpp -static -O2

daxpy-gem5: daxpy.cpp
	riscv64-unknown-linux-gnu-g++ -o daxpy-gem5 -static daxpy.cpp -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
