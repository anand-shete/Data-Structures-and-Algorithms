#include <bits/stdc++.h>

using namespace std;
// Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.


// brute force - O(n²), O(1)
int single_number_1(vector <int> &nums) {
    int n = nums.size();

    for (int i=0; i<n; ++i) {
        int cnt = 0;
        for (int j=0; j<n; ++j) {
            if (nums[i] == nums[j]) {
                cnt++;
            }
        }

        if (cnt < 2) {
            return nums[i];
        }
    }

    return -1;
}


// hashing -O(n), O(n)
int single_number_2(vector <int> &nums) {
    int n = nums.size();
    unordered_map <int, int> umap;

    for (int &x:nums) {
        umap[x]++;
    }

    for (auto [k,v]:umap) {
        if (v < 2) {
            return k;
        }
    }

    return -1;
}


// xor elements - O(n), O(1)
int single_number_3(vector <int> &nums) {
    int xored=0;

    for (int &x:nums) {
        xored ^= x;
    }

    return xored;
}

int main() {
    vector <int> nums = {1,2,1,2,4};
    // nums = {1,2,4,1,2};
    // nums = {4,1,2,1,2};

    // cout << single_number_1(nums) << endl;

    // cout << single_number_2(nums) << endl;

    cout << single_number_3(nums) << endl;


    return 0;
}