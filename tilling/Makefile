CPPFLAGS = -std=c++11 -Wall -O2
all: main.exe

main.exe: main.cc Fill.h FillC60.h Fillhexagon.h Fillpentagon.h Tiling.h
	g++ $< -o $@ $(CPPFLAGS)

