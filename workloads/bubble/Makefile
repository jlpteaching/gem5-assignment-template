GEM5_ROOT ?= ../../gem5
CROSS_COMPILE=riscv64-linux-gnu-

all: bubble

clean:
	rm -f bubble bubble-asm bubble-x86 bubble-fs

bubble: bubble.cpp
	$(CROSS_COMPILE)g++ bubble.cpp -o bubble -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum bubble

bubble-asm: bubble.cpp
	$(CROSS_COMPILE)g++ bubble.cpp -o bubble-asm -static -O2 -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm

bubble-x86:
	g++ bubble.cpp -o bubble-x86 -O2 -static -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/x86/out -lm5
	md5sum bubble-x86

bubble-fs: bubble-x86
	../make-binary-readfile.py bubble-x86 bubble-fs
	md5sum bubble-fs
