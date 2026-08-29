#include <bits/stdc++.h>

using namespace std;
// Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false. There may be duplicates in the original array.


// brute force - O(n²), O(1)
bool check_array_sorted_and_rotated_1(vector <int> nums) {
    int n = nums.size();

    for (int i=0; i<n; ++i) {
        bool sorted = 1;
        for (int j=i+1; j<i+n; ++j) {
            int prev = (j-1) % n;
            int curr = j % n;

            if (nums[prev] > nums[curr]) {
                sorted = 0;
                break;
            }
        }

        if (sorted) {
            return true;
        }
    }

    return false;
}


// O(n), O(1)
bool check_array_sorted_and_rotated_2(vector <int> &nums) {
    int drop = 0, n = nums.size();

    for (int i=1; i<n; ++i) {
        if (nums[i-1] > nums[i]) {
            drop++;
        }
    }

    if (nums[n-1] > nums[0]) {
        drop++;
    }

    return drop > 1 ? false : true;
}

int main() {
    vector <int> nums = {3,4,5,1,2};
    nums = {2,1,3,4};

    cout << check_array_sorted_and_rotated_1(nums) << endl;

    cout << check_array_sorted_and_rotated_2(nums) << endl;

    return 0;
}