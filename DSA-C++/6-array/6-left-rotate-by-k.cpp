#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums, rotate the array to the left by k steps, where k is non-negative.



// brute force - O(n), O(n)
void left_rotate_by_k_1(vector <int> &nums, int k) {
    int n = nums.size();
    vector <int> temp(n);

    for (int i=0; i<n; ++i) {
        temp[i] = nums[(i+k) % n];
    }

    for (int i=0; i<n; ++i) {
        nums[i] = temp[i];
    }
}


// In place - O(n), O(1)
void left_rotate_by_k_2(vector <int> &nums, int k) {
    int n = nums.size();
    k %= n;

    reverse(nums.begin(), nums.end());

    reverse(nums.begin(), nums.begin() + n - k);

    reverse(nums.begin() + n - k, nums.end());
}

int main() {
    vector <int> nums = {1,2};
    int k = 7;

    left_rotate_by_k_1(nums, k);
    
    // left_rotate_by_k_2(nums, k);

    for (int &x:nums) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}