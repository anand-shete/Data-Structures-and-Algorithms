#include <bits/stdc++.h>

using namespace std;

// string - O(n), O(n)
bool palindome_number_1(int num) {
    string str = to_string(num);

    reverse(str.begin(), str.end());

    return stoi(str) == num;
}


// optimal - O(log_10(n)), O(1)
bool palindrom_number_2(int num) {
    if (num < 0) return false;
    int n = num;

    long long rev = 0;
    while (num) {
        int digit = num % 10;
        rev = rev * 10 + digit;

        num /= 10;
    }

    return n == rev;
}


int main() {
    int num = 4554;
    num = 7789;
    num = 10;
    num = INT_MAX;

    // cout << palindome_number_1(num);

    cout << palindrom_number_2(num);

    cout << endl;
    return 0;
}