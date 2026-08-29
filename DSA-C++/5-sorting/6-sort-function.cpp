#include <bits/stdc++.h>

using namespace std;

int main() {
    vector <int> nums = {10,-2 ,-5 ,5 ,-20 ,1};
    
    // sort in non-decreasing order
    sort(nums.begin(), nums.end());

    // sort in decreasing order
    sort(nums.begin(), nums.end(), greater());

    // The custom function answers ONE question: "Should element 'a' come BEFORE 'b'?"
    // - Return true: Yes, 'a' comes before 'b'.
    // - Return false: No, 'a' does not come before 'b'.
    sort(nums.begin(), nums.end(), [](int a, int b) {
        return abs(a) < abs(b);
    });


    for (int &x:nums) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}