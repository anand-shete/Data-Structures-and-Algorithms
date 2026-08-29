#include <iostream>

using namespace std;
int main() {
    // In C++, any non-zero value is treated as truthy, and 0 is treated as falsy when evaluated in a boolean context



    // while loop are used when the loop ending conditions are dynamic or unknown eg. if the stop conditions depends on some variable t
    int a=1;
    while(a<2) {
        cout << "done" << endl;
        a++;
    }
    cout <<endl;



    // do while loop
    // a do while executes block of code at least once and then loops again as long as the condition is true
    int i = 0;
    do {
        cout << "hi" << endl;
        i++;
    } while (i < 0);
    cout << endl;




    // for loops should be used when you know the exact number of iterations eg. i++, i+=2, etc.
    // first the variable is initialized, then condition is checked, then loop is executed and then the value is incremented
    for (int i = 1; i <= 5; i++) {
        cout << "i="<< i << endl;
    } cout << endl;


    
    // break statement exits the nearest "loop"
    cout << "break statement: " << endl;
    for (int i = 0; i < 5; i++)   {
        for (int j = 1; j <= 100; j++) {
            cout << "j="<<j << endl;
            if (j == 2){
                break;
            }
        }
    }
    
    cout << endl;




    // continue statement skips the rest of current iteration of innermost loop and moves to the next iteration
    // for (variable ; stop condition ; inc/dec)
    for (int i = 1; i <= 5; i++) {
        if (i == 2) continue;

        cout << i << endl;
    } cout << endl;




    // switch case: switch cases based on values. Can be used to make a calculator
    i = 0;
    switch (i) {
    case 0:
        cout << "value of i is 0" << endl;
        break;

    case 1:
        cout << "value of i is 1" << endl;
        break;
    default:
        cout << "This is printed if no case is matched";
        break;
    } cout << endl;

    return 0;
}