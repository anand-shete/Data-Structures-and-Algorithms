#include <bits/stdc++.h>

using namespace std;
// Given an array containing both positive and negative integers, find the length of the longest subarray with the sum of all elements equal to zero.



// Brute force - O(n²), O(1)
int length_of_longest_subarray_with_sum_k_1(vector <int> nums, int k) {
    int ans=0, n=nums.size();

    for (int i=0; i<n; ++i) {
        int sum = 0;

        for (int j=i; j<n; ++j) {
            sum += nums[j];

            if (sum == k) {
                ans = max(ans, j-i+1);
            }
        }
    }

    return ans;
}


// Prefix sum - O(n), O(1)
int length_of_longest_subarray_with_sum_k_2(vector <int> nums, int k) {
    int ans = 0, n = nums.size(), sum=0;
    
    unordered_map <int, int> umap = {{0, -1}};

    for (int i=0; i<n; ++i) {
        sum += nums[i];

        if (umap.count(sum - k)) {
            ans = max(ans, i-umap[sum-k]);
        }

        if (!umap.count(sum)) {
            umap[sum] = i;
        }
    }

    return ans;
}

int main() {
    vector <int> nums = {10, -5, 2, 7, 1, 9};   int k = 15;
    nums = {3, 4, -1, 1, 1};    k = 5;
    nums = {6, -2, 1};      k = 5;

    cout << length_of_longest_subarray_with_sum_k_1(nums, k) << endl;

    cout << length_of_longest_subarray_with_sum_k_2(nums, k) << endl;
    
    cout << endl;
    return 0;
}