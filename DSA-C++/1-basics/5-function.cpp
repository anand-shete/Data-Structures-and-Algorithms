#include <iostream>
using namespace std;

// Function prototyping is required when function is created after main() function.
void greet(string name);


// Function overloading is when we have 2 functions of the same name and the compiler decides which one to execute at run-time.
int add(int a, int b) {
    return a + b;
}

float add(float a, float b) {
    return a + b;
}


int factorial(int x) {
    int ans = 1;
    for (int i = 1; i <= x; i++) {
        ans = ans * i;
    }
    return ans;
}

void increment_by_value(int a) {
    cout << "Inside function a=" << ++a << endl;
}

void increment_by_reference(int &b) {
    cout << "Inside function b=" << ++b << endl;
}

int main() {
    // function call
    cout << factorial(5) << endl;
    
    // void functions do not produce an output that can be used with << (stream output operator)
    greet("Abhay");
    cout << endl << endl;

    
    // Function overloading
    cout << add(4,5) << endl;
    cout << add(6.5f, 5.9f) << endl << endl;


    // When we pass a variable by value, a copy of the value is passed to the function. 
    int a = 5;
    increment_by_value(5);
    cout << "Original a=" << a << endl << endl;

    // When we pass a variable by reference, the address of the parameter is passed to the function.
    int b = 5;
    increment_by_reference(b); 
    cout << "Original b=" << b << endl << endl;  

    return 0;
}


void greet(string name) {
    cout << "Greetings, " + name;
}