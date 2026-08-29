#include <iostream> 	// unlock the classes for basic istream and ostream

using namespace std;	// hey c++, i am going to use std namespace a lot, so don't force me to write std:: every time

// The operating system calls main() function at execution
int main() {
	// << is stream insertion operator
	cout << "Enter a number: " << endl;

	// >> is stream extraction operator
	int n;
	cin >> n;

	return 0; 	// return value of main function is the exit code. It is generally not needed in C++11 and later.
}



// convert to preprocessing
// g++ -E 1-basic-program.cpp -o 1-basic-program.i

// compilation
// g++ -S 1-basic-program.i -o 1-basic-program.s

// assembly
// g++ -c 1-basic-program.s -o 1-basic-program.o

// linking
// g++ 1-basic-program.o -o a.out
