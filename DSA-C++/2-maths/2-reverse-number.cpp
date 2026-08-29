#include <bits/stdc++.h>

using namespace std;

// brute force - O(n), O(1)
int reverse_digits(int num) {
    int ans = 0;

    while (num) {
        int digit = num % 10;
        
        ans = ans * 10 + digit;
        
        num /= 10;
    }

    return ans;
}

int main() {
    int num = 12345;

    cout << reverse_digits(num);

    cout << endl;
    return 0;
}