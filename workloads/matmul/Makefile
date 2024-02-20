all: all-gem5
all-gem5: mm-ijk-gem5 mm-ijk-gem5-asm mm-ikj-gem5 mm-ikj-gem5-asm mm-block-ij-gem5 mm-block-ij-gem5-asm mm-block-ik-gem5 mm-block-ik-gem5-asm mm-block-kj-gem5 mm-block-kj-gem5-asm

clean:
	rm mm-ijk-gem5 mm-ijk-gem5-asm mm-ikj-gem5 mm-ikj-gem5-asm mm-block-ij-gem5 mm-block-ij-gem5-asm mm-block-ik-gem5 mm-block-ik-gem5-asm mm-block-kj-gem5 mm-block-kj-gem5-asm

mm-ijk-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ijk-gem5 -static -O3 -DIJK -I../include -DGEM5 -L../lib/riscv -lm5

mm-ijk-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ijk-gem5-asm -static -O3 -DIJK -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-ikj-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ikj-gem5 -static -O3 -DIKJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-ikj-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ikj-gem5-asm -static -O3 -DIKJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-ij-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ij-gem5 -static -O3 -DIJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-ij-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ij-gem5-asm -static -O3 -DIJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-ik-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ik-gem5 -static -O3 -DIK -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-ik-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ik-gem5-asm -static -O3 -DIK -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-kj-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-kj-gem5 -static -O3 -DKJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-kj-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-kj-gem5-asm -static -O3 -DKJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm
