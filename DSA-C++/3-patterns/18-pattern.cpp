#include <bits/stdc++.h>

using namespace std;

// E 
// D E 
// C D E 
// B C D E 
// A B C D E 


int main() {
    int n;
    cin >> n;

    for (int i=1; i<=n; ++i) {
        int ch = n-i+64;
        for (int j=1; j<=i; ++j) {
            cout << static_cast <char> (++ch) << " ";
        }

        cout << endl;
    }
    return 0;
}