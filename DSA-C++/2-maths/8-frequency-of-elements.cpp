#include <bits/stdc++.h>

using namespace std;

// brute force - O(n²), O(n)
vector <pair <int,int>> freq_of_elements_1(vector <int> nums) {
    vector <pair <int,int>> ans;
    int n = nums.size();
    vector <bool> visited(n, false);

    for (int i=0; i<n; ++i) {
        int cnt = 1;

        if (visited[i]) {
            continue;
        }

        for (int j=i+1; j<n; ++j) {
            if (nums[i] == nums[j]) {
                visited[j] = true;
                cnt++;
            }
        }

        ans.push_back({nums[i], cnt});
    }

    return ans;
}

// hashing - O(n), O(n)
unordered_map <int,int> freq_of_elements_2(vector <int> nums) {
    unordered_map <int,int> umap;

    for (int x:nums) {
        umap[x]++;
    }

    return umap;
}

int main() {
    vector <int> nums = {10,5,10,15,10,5};

    vector <int> ans = freq_of_elements_1(nums);
    
    // vector <int> ans = freq_of_elements_2(nums);

    for (auto [k,v]:ans) {
        cout << k << "->" << v << endl;
    }

    cout << endl;
    return 0;
}