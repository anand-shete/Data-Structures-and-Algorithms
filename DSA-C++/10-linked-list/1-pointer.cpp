#include <iostream>

using namespace std;

int main() {
    int x = 23;                     // created in stack memory
    int* h = new int(34);           // heap memory, requires manual deletion

    // Reference a variable
    cout << "memory address of x " << &x << endl;
    
    // Dereference a variable
    cout << "value stored in x " << *&x << endl;
    
    // a pointer is special variables that stores address
    int* ptr = &x;
    cout << "memory address of x " << ptr << endl;

    // dereference variables using pointer
    cout << "value stored in x " << *ptr << endl;

    // modify value using pointer
    *ptr = 10;
    cout << "updated value of x " << x << endl;

    delete h;
    
    return 0;
}