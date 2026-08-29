#include <bits/stdc++.h>

using namespace std;

// brute force - O(n), O(1)
bool is_prime_1(int num) {
    if (num < 2) return false;
    
    for (int i=2; i<num; ++i) {
        if (num % i == 0) {
            return false;
        }
    }

    return true;
}

// optimal - O(log_10 n), O(1)
bool is_prime_2(int num) {
    int divisors = 0;

    for (int i=1; i <= sqrt(num); ++i) {
        if (num % i == 0) {
            divisors++;

            if (i != num/i) {
                divisors++;
            }
        }
    }

    return divisors == 2 ? true : false;
}

int main() {
    int num = 17;
    // num = 10;

    cout << is_prime_1(num) << endl;

    cout << is_prime_2(num) << endl;

    return 0;
}