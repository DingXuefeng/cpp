CPPFLAGS = -O2 -Wall `root-config --libs` `root-config --cflags` -g
HEAD = $(shell ls *.h) 
main.exe: main.o Pentagon.o Tiling.o Hexagon.o
	g++ $^ -o $@ $(CPPFLAGS)

main.o: main.cc $(HEAD)
	g++ -c $< $(CPPFLAGS)

Pentagon.o: Pentagon.cc $(HEAD)
	g++ -c $< $(CPPFLAGS)

Hexagon.o: Hexagon.cc $(HEAD)
	g++ -c $< $(CPPFLAGS)

Tiling.o: Tiling.cc Tiling.h node.h
	g++ -c $< $(CPPFLAGS)

clean:
	-rm *.o
	-rm main.exe
	-rm *~

test: test.o Tiling.o Pentagon.o Hexagon.o
	g++ $^ -o $@ $(CPPFLAGS)

test.o: test.cc $(HEAD)
	g++ -c $< $(CPPFLAGS)

