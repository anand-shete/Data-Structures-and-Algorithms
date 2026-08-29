#include <iostream>

using namespace std;

// O(5^(n/2). 4^(n/2)), O(n)
int count_good_numbers (int idx, int n) {
    // A good number is a number whoose even places are even and odd places are prime
    // to avoid overflow, return ans * MOD(10^9 + 7)
    
    if (idx == n) return 1;

    int ans = 0;
    const int MOD = 1e9 + 7;

    if (idx % 2 == 0) {
        for (int dig:{0,2,4,6,8}) {
            ans += count_good_numbers(idx+1, n);
            ans %= MOD;
        }
    }
    else {
        for (int dig:{2,3,5,7}) {
            ans += count_good_numbers(idx+1, n);
            ans %= MOD;
        }
    }

    return ans;
}

int main() {
    int n = 4;

    cout << count_good_numbers(0,n) << endl;

    return 0;
}