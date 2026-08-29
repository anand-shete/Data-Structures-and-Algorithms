#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums, find the subarray with the largest sum and print all elements present in subarray.


// brute force - O(n²), O(1)
void print_max_subarray_sum_1(vector <int> &nums) {
    int n = nums.size(), start, end, max_sum;
    start = end = 0;
    max_sum = INT_MIN;

    if (nums.empty()) return;

    for (int i=0; i<n; ++i) {
        int sum = 0;

        for (int j=i; j<n; ++j) {
            sum += nums[j];

            if (sum > max_sum) {
                max_sum = sum;
                start = i;
                end = j;
            }
        }
    }

    for (int i=start; i<=end; ++i) {
        cout << nums[i] << " ";
    }
    
    cout << endl;
}


// kadane - O(n), O(1)
void print_max_subarray_sum_2(vector <int> &nums) {
    int n = nums.size(), sum, max_sum, start, temp_start, end;
    start = temp_start = end = sum = 0;
    max_sum = INT_MIN;

    if (nums.empty()) return;

    for (int i=0; i<n; ++i) {
        sum += nums[i];

        if (sum > max_sum) {
            max_sum = sum;
            start = temp_start;
            end = i;
        }

        if (sum < 0) {
            sum = 0;
            temp_start = i+1;
        }
    }

    for (int i=start; i<=end; ++i) {
        cout << nums[i] << " ";
    }
 
    cout << endl;
}

int main() {
    vector <int> nums = {2, 3, 5, -2, 7, -4};
    nums = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    // nums = {-3, -2, -5};
    nums = {-2, 0, -1};
    // nums = {};
    
    print_max_subarray_sum_1(nums);

    print_max_subarray_sum_2(nums);

    return 0;
}