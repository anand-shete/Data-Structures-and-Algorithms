#include <bits/stdc++.h>

using namespace std;

// A
// BB
// CCC
// DDDD
// EEEEE


int main() {
    int n;
    cin >> n;

    for (int i=1; i<=n; ++i) {
        
        for (int j=1; j<=i; ++j) {
            cout << static_cast <char> (i+64);
        }

        cout << endl;
    }

    return 0;
}