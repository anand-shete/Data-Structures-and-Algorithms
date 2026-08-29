#include <bits/stdc++.h>

using namespace std;


// O(n), O(1)
int nth_root_of_m_1 (int n, int m) {
    int ans = -1;

    for (int i=0; i<m; i++) {
        int x = pow(i,n);
        if (x == m) ans = i;
    }

    return ans;
}

// O(logn), O(1)
int nth_root_of_m_2 (int n, int m) {
    int ans = 1;
    int low = 0, high = m;

    while (low <= high) {
        int mid = low + (high-low) / 2;

        for (int i=1; i<n ;i++) {
            ans = ans * i;
            if (ans > m) break;
        }

        if (ans == m) return mid;
        else if (ans < m) low = mid+1;
        else high = mid-1;
    }

    return -1;
}



int main() {
    vector <int> arr = {3, 4, 4, 7, 8, 10};
    int m = 32, n = 4;

    cout << nth_root_of_m_1(n, m) << endl;
    // cout << nth_root_of_m_2(n, m) << endl;

    return 0;
}