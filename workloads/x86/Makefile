all: all-native
all-native: mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-kj-native

clean:
	rm mm-ijk-native mm-ikj-native mm-block-ij-native mm-block-ik-native mm-block-kj-native

mm-ijk-native: mm.cpp
	g++ mm.cpp -o mm-ijk-native -static -O3 -DIJK

mm-ikj-native: mm.cpp
	g++ mm.cpp -o mm-ikj-native -static -O3 -DIKJ

mm-block-ij-native: mm.cpp
	g++ mm.cpp -o mm-block-ij-native -static -O3 -DIJ

mm-block-ik-native: mm.cpp
	g++ mm.cpp -o mm-block-ik-native -static -O3 -DIK

mm-block-kj-native: mm.cpp
	g++ mm.cpp -o mm-block-kj-native -static -O3 -DKJ
