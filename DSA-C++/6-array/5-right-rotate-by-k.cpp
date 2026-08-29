#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.


// Brute force - O(n), O(n)
void right_rotate_by_k_1(vector <int> &nums, int k) {
    int n = nums.size();
    vector <int> temp(n);

    for (int i=0; i<n; ++i) {
        temp[i] = nums[(i+n-k) % n];
    }

    for (int i=0; i<n; ++i) {
        nums[i] = temp[i];
    }
}


// In place - O(n), O(1)
void right_rotate_by_k_2(vector <int> &nums, int k) {
    int n = nums.size();

    reverse(nums.begin(), nums.end());

    reverse(nums.begin(), nums.begin() + k);

    reverse(nums.begin()+k, nums.end());
}

int main() {
    vector <int> nums = {1,2,3,4,5,6,7};
    int k=3;

    // right_rotate_by_k_1(nums, k);`

    right_rotate_by_k_2(nums, k);

    for (int &x:nums) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}