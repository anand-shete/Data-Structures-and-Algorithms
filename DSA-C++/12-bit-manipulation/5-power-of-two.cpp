#include <bits/stdc++.h>

using namespace std;

// Given an integer n, return true if it is a power of two. Otherwise, return false. An integer n is a power of two if there exists an integer x such that n == 2ˣ

// brute force - 
bool power_of_two_1(int n) {
    
    for (int i=0; i<=30; ++i) {
        int num = pow(2,i);

        if (num == n) {
            return true;
        }
    }
    
    return false;
}

int main() {
    int n = 16;
    
    cout << power_of_two_1(n) << endl;


    return 0;
}