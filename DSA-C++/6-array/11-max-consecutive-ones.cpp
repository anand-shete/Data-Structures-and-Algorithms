#include <bits/stdc++.h>

using namespace std;
// Given an array that contains only 1 and 0 return the count of maximum consecutive ones in the array..


// brute force - O(n), O(1)
int max_consecutive_ones(vector <int> &nums) {
    int n = nums.size(), max_ones = 0, cnt = 0;

    for (int i=0; i<n; ++i) {
        if (nums[i] == 0 && cnt > max_ones) {
            max_ones = cnt;
            cnt = 0;
        }
        else {
            cnt++;
        }
    }

    if (cnt > max_ones) {
        max_ones = cnt;
    }

    return max_ones;
}

int main() {
    vector <int> nums = {1, 1, 0, 1, 1, 1};
    
    cout << max_consecutive_ones(nums) << endl;

    return 0;
}