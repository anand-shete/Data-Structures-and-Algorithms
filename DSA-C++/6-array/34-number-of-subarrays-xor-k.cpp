#include <bits/stdc++.h>

using namespace std;

// brute force - O(n²), O(1)
int number_of_subarrays_that_xor_k_1(vector <int> nums, int k) {
    int ans=0, n = nums.size();

    for (int i=0; i<n; ++i) {
        int xore = 0;

        for (int j=i; j<n; ++j) {
            xore ^= nums[j];

            if (xore == k) {
                ans++;
            }
        }
    }

    return ans;
}

// prefix sum - O(n), O(1)
int number_of_subarrays_that_xor_k_2(vector <int> nums, int k) {
    int ans = 0, n = nums.size(), xored=0;
    unordered_map <int, int> umap = {{0,1}};

    for (int i=0; i<n; ++i) {
        xored ^= nums[i];

        if (umap.count(xored^k)) {
            ans += umap[xored^k];
        }

        umap[xored]++;
    }
    
    return ans;
}


int main() {
    vector <int> nums = {4, 2, 2, 6, 4};
    int k = 6;

    // cout << number_of_subarrays_that_xor_k_1(nums, k);

    cout << number_of_subarrays_that_xor_k_2(nums, k);

    cout << endl;
    return 0;
}