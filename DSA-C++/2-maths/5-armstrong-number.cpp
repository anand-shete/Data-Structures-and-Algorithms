#include <bits/stdc++.h>

using namespace std;
// Q. given a number, return true if its armstrong, false otherwise

// logarithmic - O(log_10 n), O(1)
bool armstrong_number(int num) {
    int temp = num;
    int cubed = 0;

    while (temp) {
        int digit = temp % 10;
        cubed += digit * digit * digit;

        temp /= 10;
    }

    return cubed == num;
}

int main() {
    int num = 153;
    num = 371;
    // num = 12;

    cout << armstrong_number(num) << endl;

    return 0;
}