#include <bits/stdc++.h>

using namespace std;
// Given an array nums of size n, return the majority element. The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.


// brute force - O(n²), O(1)
int majority_element_1(vector <int> &nums) {
    int n = nums.size(), max_cnt=0, maj_ele=nums[0];

    for (int i=0; i<n; ++i) {
        int cnt = 0;

        for (int j=0; j<n; ++j) {
            if (nums[i] == nums[j]) {
                cnt++;
            }
        }

        if (cnt > max_cnt) {
            max_cnt = cnt;
            maj_ele = nums[i];
        }
    }
    
    return max_cnt > n/2 ? maj_ele : -1;
}


// hashing - O(n), O(n)
int majority_element_2(vector <int> &nums) {
    int n = nums.size(), max_freq=0, maj_ele=nums[0];
    unordered_map <int,int> umap;

    for (int &x:nums) {
        umap[x]++;
    }

    for (auto [k,v]:umap) {
        if (v > max_freq) {
            max_freq = v;
            maj_ele = k;
        }
    }

    return max_freq > n/2 ? maj_ele : -1;
}


// Boyer-Moore Majority Vote Algorithm - O(n), O(1)
int majority_element_3(vector <int> nums) {
    int n = nums.size(), cnt=0, ele=nums[0];

    for (int i=0; i<n; ++i) {
        if (cnt == 0) {
            ele = nums[i];
            cnt++;
        }
        else if (ele != nums[i]) {
            cnt--;
        }
        else {
            cnt++;
        }
    }


    // verify
    cnt = 0;
    for (int &x:nums) {
        if (x == ele) {
            cnt++;
        }
    }

    return cnt > n/2 ? ele : -1;
}

int main() {
    vector <int> nums = {2, 2, 1, 1, 1, 2, 2};
    nums = {7, 7, 7, 7, 7};
    nums = {1, 2, 1, 3, 1, 4, 1};
    nums = {1, 2, 3, 4, 9, 9, 9, 9, 9};
    // nums = {1, 2, 3};       // edge case: majority element does not exists

    
    cout << majority_element_1(nums) << endl;
    
    cout << majority_element_2(nums) << endl;

    cout << majority_element_3(nums) << endl;


    return 0;
}