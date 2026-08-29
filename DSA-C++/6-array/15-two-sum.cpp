#include <bits/stdc++.h>

using namespace std;
// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
// You can return the answer in any order.


// brute force - O(n²), O(1)
pair <int, int> two_sum_1(vector <int> &nums, int target) {
    int n = nums.size();
    
    for (int i=0; i<n; ++i) {

        for (int j=i+1; j<n; ++j) {
            if (nums[i] + nums[j] == target) {
                return {i,j};
            }
        }
    }

    return {};
}


// two pointers - O(n. log n), O(n)
pair <int,int> two_sum_2(vector <int> &nums, int target) {
    int n = nums.size();
    int left=0, right=n-1;
    vector <pair <int,int>> indexed;

    for (int i=0; i<n; ++i) {
        indexed.push_back({nums[i], i});
    }

    sort(indexed.begin(), indexed.end());

    while (left < right) {
        int sum = indexed[left].first + indexed[right].first;

        if (sum < target) {
            left++;
        }
        else if (sum > target) {
            right--;
        }
        else {
            return {indexed[left].second, indexed[right].second};
        }
    }

    return {};
}


// hashing
pair <int,int> two_sum_3(vector <int> &nums, int target) {
    int n = nums.size();
    unordered_map <int,int> umap;

    int i= 0;
    for (int &x:nums) {
        
        if (umap.count(target-x)) {
            return {i, umap[target-x]};
        }
        
        umap[x] = i++;
    }

    return {};
}

int main() {
    vector <int> nums = {2,7,11,15}; int target = 9;
    // nums = {3,2,4}; target = 6;
    // nums = {3,3}; target = 6;

    // auto [n1, n2] = two_sum_1(nums, target);

    // auto [n1, n2] = two_sum_2(nums, target);

    auto [n1, n2] = two_sum_3(nums, target);

    cout << n1 << " " << n2 << endl;

    return 0;
}