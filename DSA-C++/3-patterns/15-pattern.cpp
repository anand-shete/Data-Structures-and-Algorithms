#include <bits/stdc++.h>

using namespace std;

// ABCDE
// ABCD
// ABC
// AB
// A

int main() {
    int n;
    cin >> n;

    for (int i=n; i>=1; --i) {
        int c = 64;
        for (int j=i; j>=1; --j) {
            cout << static_cast <char> (++c);
        }

        cout << endl;
    }

    return 0;
}