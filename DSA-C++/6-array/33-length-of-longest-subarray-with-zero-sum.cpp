#include <bits/stdc++.h>

using namespace std;

// Brute force - O(n²), O(1)
int length_of_longest_subarray_with_zero_sum_1(vector <int> nums) {
    int ans = 0, sum = 0, n = nums.size();

    for (int i=0; i<n; ++i) {
        int sum = 0;

        for (int j=i; j<n; ++j) {
            sum += nums[j];

            if (sum == 0) {
                ans = max(ans, j-i+1);
            }
        }
    }

    return ans;
}

// Prefix sum - O(n), O(1)
int length_of_longest_subarray_with_zero_sum_2(vector <int> nums) {
    int ans = 0, sum = 0, n=nums.size();
    unordered_map <int, int> umap = {{0,-1}};

    for (int i=0; i<n; ++i) {
        sum += nums[i];

        if (umap.count(sum)) {
            ans = max(ans, i-umap[sum]);
        }
        else {
            umap[sum] = i;
        }
    }

    return ans;
}

int main() {
    vector <int> nums = {9, -3, 3, -1, 6, -5};

    // cout << length_of_longest_subarray_with_zero_sum_1(nums);
    
    cout << length_of_longest_subarray_with_zero_sum_2(nums);

    cout << endl;
    return 0;
}