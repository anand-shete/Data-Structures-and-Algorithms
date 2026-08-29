#include <bits/stdc++.h>

using namespace std;
// Given two integers n and i, return true if the ith bit in the binary representation of n (counting from the least significant bit, 0-indexed) is set (1). Otherwise, return false.

// suboptimal - O(log_2 n), O(log_2 n)
bool check_ith_bit_set_1(int n, int i) {
    string bin = "";

    while (n) {
        bin += n % 2 == 0 ? '0' : '1';
        n /= 2;
    }

    if (i > bin.size()) {
        return false;
    }

    return bin[i] == '1' ? true : false;
}


// optimal - O(1), O(1)
bool check_ith_bit_set_2(int n, int i) {
    return (n >> i) & 1;
}

int main() {
    int n = 5, i = 1;

    cout << check_ith_bit_set_1(n, i) << endl;  

    cout << check_ith_bit_set_2(n, i) << endl;

    return 0;
}