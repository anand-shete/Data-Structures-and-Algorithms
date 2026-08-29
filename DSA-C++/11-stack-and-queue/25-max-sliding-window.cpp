#include <bits/stdc++.h>

using namespace std;

// You are given an array of integers nums, there is a sliding window of size `k` which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

// Return the maximum of sliding window.


// brute force - O(n²), O(1)
vector <int> sliding_window_maximum_1(vector <int> &nums, int k) {
    int n = nums.size();
    vector <int> ans;

    for (int i=0; i<=n-k; ++i) {
        int maxi = nums[i];

        for (int j=i; j<i+k; ++j) {
            if (nums[j] > maxi) {
                maxi = nums[j];
            }
        }

        ans.push_back(maxi);
    }

    return ans;
}


// stack - O(n), O(1)
vector <int> sliding_window_maximum_2(vector <int> nums, int k) {
    int n = nums.size();
    vector <int> ans;
    deque <int> dq;

    for (int i=0; i<n; ++i) {
        // sliding window is from i-k+1 to i
        if (!dq.empty() && dq.front() < i-k+1) {
            dq.pop_front();
        }

        while (!dq.empty() && nums[dq.back()] < nums[i]) {
            dq.pop_back();
        }

        dq.push_back(i);

        if (i-k+1 >= 0) {
            ans.push_back(nums[dq.front()]);
        }
    }

    return ans;
}


int main() {
    vector <int> nums = {4, 0, -1, 3, 5, 3, 6, 8};
    nums = {1, 3, -1, -3, 5, 3, 6, 7};
    
    int k = 3;

    // vector <int> ans = sliding_window_maximum_1(nums, k);

    vector <int> ans = sliding_window_maximum_2(nums, k);

    for (int x:ans) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}