#include <bits/stdc++.h>

using namespace std;

//     A
//    ABA
//   ABCBA
//  ABCDCBA
// ABCDEDCBA


int main() {
    int n;
    cin >> n;

    for (int i=1; i<=n; ++i) {
        int c = 64;

        for (int j=1; j<=n-i; ++j) {
            cout << " ";
        }

        for (int j=n-i+1; j<=n; ++j) {
            cout << static_cast<char>(++c);
        }

        for (int j=1; j<i; ++j) {
            cout << static_cast<char>(--c);
        }
        cout << endl;
    }
    
    return 0;
}