GEM5_ROOT ?= ../../gem5

all: mm mm-O0 mm-O3

clean:
	rm mm mm-O0 mm-O3

mm: mm.cpp
	riscv64-linux-gnu-g++ -o mm mm.cpp -static -O2

mm-O0: mm.cpp
	riscv64-linux-gnu-g++ -o mm-O0 mm.cpp -static -O0

mm-O3: mm.cpp
	riscv64-linux-gnu-g++ -o mm-O3 mm.cpp -static -O3
