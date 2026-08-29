#include <iostream>
using namespace std;
// TODO basic recursion from 1st section


int count = 0;
void func() {
    if(count ==3) return;
    cout << count << " ";
    count++;
    func();
}

// forward recursion e.g.
void printName(int count, int n) {

    // If count equals n, return to previous call
    if (count == n) return;

    cout << "anand" << endl;
    printName(count+1,n);
}

void printNum(int c, int n) {
    if(c > n) return;

    cout << c;
    printNum(c+1,n);
}


// backward recursion (backtracking recursion)
void backPrintNum(int c,int n) {

    if(c < 1) return;

    cout << c;
    backPrintNum(c-1,n);
}

int main() {
    cout << "Enter n: ";
    int n;
    cin >>n;
    // func();

    // printName(0,4);
    // printNum(1,n);

    backPrintNum(n,n);

    cout << endl;
    return 0;
}