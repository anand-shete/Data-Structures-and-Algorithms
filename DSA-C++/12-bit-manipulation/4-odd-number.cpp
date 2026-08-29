#include <bits/stdc++.h>

using namespace std;
// Given a non-negative integer n, determine whether it is odd. Return true if the number is odd, otherwise return false. A number is odd if it is not divisible by 2 (i.e., n % 2 != 0).


// O(1), O(1)
bool odd_number(int n) {
    return n % 2 == 1;
}

int main() {
    int n = -5;

    cout << odd_number(n) << endl;

    return 0;
}