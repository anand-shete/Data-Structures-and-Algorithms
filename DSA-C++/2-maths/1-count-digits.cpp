#include <bits/stdc++.h>

using namespace std;

// string - O(n), O(n)
int count_digits_1(int num) {
    string str = to_string(abs((long long)num));

    return str.size();
}

// brute force - O(log_10(n) + 1), O(1)
int count_digits_2(int num) {
    if (num == 0) return 1;

    int ans = 0;

    while (num) {
        ans++;
        num /= 10;
    }

    return ans;
}

// log function - O(1), O(1)
int count_digits_3(int num) {
    if (num == 0) return 1;

    int count = log10(abs((long long)num)) + 1;

    return (int)(count);
}

int main() {
    int num1 = 1000;
    int num2 = 12345;
    int num3 = INT_MIN;

    cout << count_digits_1(num3);

    // cout << count_digits_2(num3);

    // cout << count_digits_3(num3);

    cout << endl;
    return 0;
}