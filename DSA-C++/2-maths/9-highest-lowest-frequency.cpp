#include <bits/stdc++.h>

using namespace std;

// brute force - O(n²), O(1)
pair <int, int> highest_lowest_freq_1(vector <int> nums) {
    int low=INT_MAX, high=INT_MIN, n=nums.size();
    pair <int,int> p = {low, high};

    for (int i=0; i<n; ++i) {
        int cnt = 1;

        for (int j=i+1; j<n; ++j) {
            if (nums[i] == nums[j]) {
                cnt++;
            }
        }

        if (cnt < p.first) p.first = nums[i];
        if (cnt > p.second) p.second = nums[i];
    }

    return p;
}

// hashing - O(n), O(n)
pair <int,int> highest_lowest_freq_2(vector <int> nums) {
    unordered_map <int, int> umap;
    int lowestFreq =INT_MAX, highestFreq=0, minEle=INT_MAX, maxEle=INT_MIN;
    
    for (int x:nums) {
        umap[x]++;
    }

    for (auto [k,v]:umap) {
        if (v < lowestFreq) {
            minEle = k;
            lowestFreq = v;
        }
        if (v > highestFreq) {
            maxEle = k;
            highestFreq = v;
        }
    }

    return {minEle, maxEle};
}

int main() {
    vector <int> nums = {10,5,10,15,10,5};
    // vector <int> nums = {2,2,2};

    // auto [f,s] = highest_lowest_freq_1(nums);
    // cout << f << " " << s << endl;


    auto [f,s] = highest_lowest_freq_2(nums);
    cout << f << " " << s << endl;

    return 0;
}