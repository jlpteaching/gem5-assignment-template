GEM5_ROOT ?= ../../gem5
CROSS_COMPILE=riscv64-linux-gnu-

all: all-gem5
all-gem5: mm-ijk-gem5 mm-ikj-gem5 mm-block-ij-gem5 mm-block-ik-gem5 mm-block-jk-gem5
all-native: mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-jk-native

clean:
	rm mm-ijk-gem5 mm-ijk-gem5-asm mm-ikj-gem5 mm-ikj-gem5-asm mm-block-ij-gem5 mm-block-ij-gem5-asm mm-block-ik-gem5 mm-block-ik-gem5-asm mm-block-jk-gem5 mm-block-jk-gem5-asm
	rm mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-jk-native

mm-ijk-native: mm.cpp
	g++ mm.cpp -o mm-ijk-native -static -O3 -DIJK

mm-ijk-gem5: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-ijk-gem5 -static -O3 -DIJK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum mm-ijk-gem5

mm-ijk-gem5-asm: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-ijk-gem5-asm -static -O3 -DIJK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm

mm-ikj-native: mm.cpp
	g++ mm.cpp -o mm-ikj-native -static -O3 -DIKJ

mm-ikj-gem5: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-ikj-gem5 -static -O3 -DIKJ -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum mm-ikj-gem5

mm-ikj-gem5-asm: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-ikj-gem5-asm -static -O3 -DIKJ -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm

mm-block-ij-native: mm.cpp
	g++ mm.cpp -o mm-block-ij-native -static -O3 -DIJ

mm-block-ij-gem5: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-ij-gem5 -static -O3 -DIJ -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum mm-block-ij-gem5

mm-block-ij-gem5-asm: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-ij-gem5-asm -static -O3 -DIJ -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm

mm-block-ik-native: mm.cpp
	g++ mm.cpp -o mm-block-ik-native -static -O3 -DIK

mm-block-ik-gem5: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-ik-gem5 -static -O3 -DIK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum mm-block-ik-gem5

mm-block-ik-gem5-asm: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-ik-gem5-asm -static -O3 -DIK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm

mm-block-jk-native: mm.cpp
	g++ mm.cpp -o mm-block-jk-native -static -O3 -DJK

mm-block-jk-gem5: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-jk-gem5 -static -O3 -DJK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5
	md5sum mm-block-jk-gem5

mm-block-jk-gem5-asm: mm.cpp
	$(CROSS_COMPILE)g++ mm.cpp -o mm-block-jk-gem5-asm -static -O3 -DJK -I$(GEM5_ROOT)/include -DGEM5 -L$(GEM5_ROOT)/util/m5/build/riscv/out -lm5 -S -fverbose-asm
