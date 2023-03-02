all: all-gem5 all-native
all-gem5: mm-ijk-gem5 mm-ijk-gem5-asm mm-ikj-gem5 mm-ikj-gem5-asm mm-block-ij-gem5 mm-block-ij-gem5-asm mm-block-ik-gem5 mm-block-ik-gem5-asm mm-block-kj-gem5 mm-block-kj-gem5-asm
all-native: mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-kj-native

clean:
	rm mm-ijk-gem5 mm-ijk-gem5-asm mm-ikj-gem5 mm-ikj-gem5-asm mm-block-ij-gem5 mm-block-ij-gem5-asm mm-block-ik-gem5 mm-block-ik-gem5-asm mm-block-kj-gem5 mm-block-kj-gem5-asm
	rm mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-kj-native

mm-ijk-native: mm.cpp
	g++ mm.cpp -o mm-ijk-native -static -O3 -DIJK

mm-ijk-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ijk-gem5 -static -O3 -DIJK -I../include -DGEM5 -L../lib/riscv -lm5

mm-ijk-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ijk-gem5-asm -static -O3 -DIJK -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-ikj-native: mm.cpp
	g++ mm.cpp -o mm-ikj-native -static -O3 -DIKJ

mm-ikj-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ikj-gem5 -static -O3 -DIKJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-ikj-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-ikj-gem5-asm -static -O3 -DIKJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-ij-native: mm.cpp
	g++ mm.cpp -o mm-block-ij-native -static -O3 -DIJ

mm-block-ij-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ij-gem5 -static -O3 -DIJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-ij-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ij-gem5-asm -static -O3 -DIJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-ik-native: mm.cpp
	g++ mm.cpp -o mm-block-ik-native -static -O3 -DIK

mm-block-ik-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ik-gem5 -static -O3 -DIK -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-ik-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-ik-gem5-asm -static -O3 -DIK -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm

mm-block-kj-native: mm.cpp
	g++ mm.cpp -o mm-block-kj-native -static -O3 -DKJ

mm-block-kj-gem5: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-kj-gem5 -static -O3 -DKJ -I../include -DGEM5 -L../lib/riscv -lm5

mm-block-kj-gem5-asm: mm.cpp
	riscv64-linux-gnu-g++ mm.cpp -o mm-block-kj-gem5-asm -static -O3 -DKJ -I../include -DGEM5 -L../lib/riscv -lm5 -S -fverbose-asm
