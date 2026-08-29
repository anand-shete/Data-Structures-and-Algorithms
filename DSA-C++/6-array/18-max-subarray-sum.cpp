#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums, find the subarray with the largest sum and return the sum of the elements present in that subarray. A subarray is a contiguous non-empty sequence of elements within an array.




// Brute force - O(n²), O(1)
int max_subarray_sum_1(vector <int> &nums) {
    int n = nums.size(), max_sum=INT_MIN;

    for (int i=0; i<n; ++i) {
        int sum =0;

        for (int j=i; j<n; ++j) {
            sum += nums[j];

            if (sum > max_sum) {
                max_sum = sum;
            }
        }
    }

    return max_sum;
}


// Kadane algorithm - O(n), O(1)
int max_subarray_sum_2(vector <int> &nums) {
    int max_sum = INT_MIN, sum = 0;
    
    for (int x:nums) {
        sum += x;

        if (sum > max_sum) {
            max_sum = sum;
        }

        if (sum < 0) {
            sum = 0;
        }
    }

    return max_sum;
}

int main() {
    vector <int> nums = {2, 3, 5, -2, 7, -4};
    nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    nums = {-3, -2, -5};
    // nums = {-2, 0, -1};
    // nums = {};

    cout << max_subarray_sum_1(nums) << endl;

    cout << max_subarray_sum_2(nums) << endl;

    return 0;
}