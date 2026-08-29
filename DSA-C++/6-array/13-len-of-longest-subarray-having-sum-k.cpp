#include <bits/stdc++.h>

using namespace std;
// Given an array nums of size n containing only positive elments and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.



// brute force - O(n²), O(1)
int len_of_longest_subarray_having_sum_k_1(vector <int> &nums, int k) {
    int n = nums.size(), max_len=0;

    for (int i=0; i<n; ++i) {
        int sum = 0;

        for (int j=i; j<n; ++j) {
            sum += nums[j];

            if (sum == k) {
                max_len = max(max_len, j-i+1);
            }
        }
    }

    return max_len;
}

// prefix sum - O(n), O(n)
int len_of_longest_subarray_having_sum_k_2(vector <int> &nums, int k) {
    int sum = 0, n = nums.size(), max_len = 0;
    unordered_map <int, int> umap = {{0, -1}};

    for (int i=0; i<n; ++i) {
        sum += nums[i];

        if (umap.count(sum - k)) {
            max_len = max(max_len, i - umap[sum - k]);
        }

        if (!umap.count(sum)) {
            umap[sum] = i;
        }
    }

    return max_len;
}


// sliding window - O(n), O(1)
int len_of_longest_subarray_having_sum_k_3(vector <int> &nums, int k) {
    int n = nums.size(), left, sum, max_len;
    left = sum = max_len = 0;

    for (int right=left; right<n; ++right) {
        sum += nums[right];

        while (sum > k) {
            sum -= nums[left];
            left++;
        }

        if (sum == k) {
            max_len = max(max_len, right-left+1);
        }
    }

    return max_len;
}


int main() {
    vector <int> nums = {10, 5, 2, 7, 1, 9}; int k = 15;
    nums = {4, 2, 4, 4, 7, 3, 9, 3}; k = 7;
    // nums = {-3, 2, 1}; k = 6;
    
    // cout << len_of_longest_subarray_having_sum_k_1(nums, k) << endl;

    // cout << len_of_longest_subarray_having_sum_k_2(nums, k) << endl;

    cout << len_of_longest_subarray_having_sum_k_3(nums, k) << endl;

    return 0;
}