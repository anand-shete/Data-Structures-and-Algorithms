#include <bits/stdc++.h>

using namespace std;

// O(log_2 n), O(1)
string decimal_to_binary(int n) {
    string ans = "";

    if (n == 0) {
        return "0";
    }

    while (n) {
        int rem = n % 2;
        ans += to_string(rem);
        n /= 2;
    }

    reverse(ans.begin(), ans.end());

    return ans;
}


int main() {
    int n;
    cin >> n;

    cout << decimal_to_binary(n) << endl;

    return 0;
}