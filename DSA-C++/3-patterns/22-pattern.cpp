#include <bits/stdc++.h>

using namespace std;

// 4 4 4 4 4 4 4 
// 4 3 3 3 3 3 4 
// 4 3 2 2 2 3 4 
// 4 3 2 1 2 3 4 
// 4 3 2 2 2 3 4 
// 4 3 3 3 3 3 4 
// 4 4 4 4 4 4 4 


int main() {
    int n;
    cin >> n;

    for (int i=0; i<2*n-1; ++i) {
        for (int j=0; j<2*n-1; ++j) {
            int top = i;
            int left = j;
            int btm = (2 * n - 2) - i;
            int right = (2 * n - 2) - j;
            
            int mini = min(min(top, btm), min(left, right));

            cout << n-mini << " ";
        }

        cout << endl;
    }

    return 0;
}