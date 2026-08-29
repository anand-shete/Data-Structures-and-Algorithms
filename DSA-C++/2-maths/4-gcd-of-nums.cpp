#include <bits/stdc++.h>

using namespace std;

// brute force - O(min(num1,num2)), O(1)
int gcd_of_nums_1(int num1, int num2) {
    int start = min(num1,num2), ans;

    for (int i=start; i>=1; --i) {
        if (num1 % i == 0 && num2 % i == 0) {
            ans = i;
            break;
        }
    }

    return ans;
}

// euclidean algorithm - O(log_10(min(mum1, num2))), O(1)
int gcd_of_nums_2(int num1, int num2) {
    while (num1>0 && num2>0) {
        if (num1>num2) {
            num1 %= num2;
        }
        else {
            num2 %= num1;
        }
    }

    return num1 > num2 ? num1 : num2;
}


int main() {
    int num1=9, num2=12;
    // num1=20, num2=15;

    // cout << gcd_of_nums_1(num1, num2) << endl;
    
    cout << gcd_of_nums_2(num1, num2) << endl;
    
    return 0;
}