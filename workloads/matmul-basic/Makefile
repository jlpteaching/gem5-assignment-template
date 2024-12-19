GEM5_ROOT ?= ../../gem5

all: mm-riscv mm-arm mm-x86

clean:
	rm mm-riscv mm-arm mm-x86

mm-riscv: mm.cpp $(GEM5_ROOT)/util/m5/build/riscv/out/libm5.a
	riscv64-linux-gnu-g++ -o mm-riscv mm.cpp -DGEM5 -std=c++11 -I$(GEM5_ROOT)/include -L$(GEM5_ROOT)/util/m5/build/riscv/out/ -lm5 -static
	md5sum mm-riscv

mm-arm: mm.cpp $(GEM5_ROOT)/util/m5/build/arm64/out/libm5.a
	aarch64-linux-gnu-g++ -o mm-arm mm.cpp -DGEM5 -std=c++11 -I$(GEM5_ROOT)/include -L$(GEM5_ROOT)/util/m5/build/arm64/out/ -lm5 -static
	md5sum mm-arm

mm-x86: mm.cpp $(GEM5_ROOT)/util/m5/build/x86/out/libm5.a
	g++ -o mm-x86 mm.cpp -DGEM5 -std=c++11 -I$(GEM5_ROOT)/include -L$(GEM5_ROOT)/util/m5/build/x86/out/ -lm5 -static
	md5sum mm-x86

mm-x86.s: mm-x86
	objdump -S mm-x86 | grep _Z8multiplyPPdS0_S0_i -A100 -m1 > mm-x86.s

mm-arm.s: mm-arm
	aarch64-linux-gnu-objdump -S mm-arm | grep _Z8multiplyPPdS0_S0_i -A100 -m1 > mm-arm.s

mm-riscv.s: mm-riscv
	riscv64-linux-gnu-objdump -S mm-riscv | grep _Z8multiplyPPdS0_S0_i -A100 -m1 > mm-riscv.s
