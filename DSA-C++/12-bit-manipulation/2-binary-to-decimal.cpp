#include <bits/stdc++.h>

using namespace std;

// O(n), O(1)
int binary_to_decimal(string n) {
    int ans = 0, pow2 = 1;
    
    for (int i=n.size()-1; i>=0; --i) {
        if (n[i] == '1') {
            ans += pow2;
        }

        pow2 *= 2;
    }

    return ans;
}

int main() {
    int n;
    cin >> n;

    cout << binary_to_decimal(to_string(n)) << endl;

    return 0;
}