This CPPGenerator is used to generate C++ source codes, which include *.cpp, and *.hpp, their tests(googletest) and corresponding makefile content.
We could use this tool to eliminate the routine work which we must do when creating a new class in our source tree.
The primary tasks it could help us do include:
1. The main input parameter for this tool is the "class" name;
2. It could generate the class.cpp(in ./src directory), class.hpp(in ./inc directory);
3. It could change the Makefile which could help me finish the codes in Makefile on compiling and linking the class.cpp file;
4. It also could generate template codes for testClass.cpp, which will use GoogleTest framework to implement the testing logic. The real testing logic should be designed mannually.

   zhong.clock@gmail.com

