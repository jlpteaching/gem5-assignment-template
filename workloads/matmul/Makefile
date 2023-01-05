GEM5_ROOT ?= ../../gem5

all: mm mm-gem5

clean:
	rm mm mm-gem5

mm: mm.cpp
	riscv64-unknown-linux-gnu-g++ -o mm mm.cpp -static -O2

mm-gem5: mm.cpp
	riscv64-unknown-linux-gnu-g++ -o mm-gem5 -static mm.cpp -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
