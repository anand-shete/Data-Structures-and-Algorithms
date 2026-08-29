#include <bits/stdc++.h>

using namespace std;

// Q. Problem Statement: Given an array of integers arr of size n, calculate the sum of the minimum value in each (contiguous) subarray of arr. Since the result may be large, return the answer modulo 10⁹ +7.

const int MOD = 1e9 + 7;

// brute force - O(n²), O(1)
int sum_of_subarray_minimums_1(vector <int> nums) {
    int n = nums.size();
    int ans = 0;

    for (int i=0; i<n; ++i) {
        int mini = INT_MAX;

        for (int j=i; j<n; ++j) {
            if (nums[j] < mini) {
                mini = nums[j];
            }

            ans = (ans + mini) % MOD;
        }
    }

    return ans;
}

// stack - O(n), O(n)
int sum_of_subarray_minimums_2(vector <int> nums) {
    int n = nums.size();
    long long ans = 0;
    vector <int> min_prev(n, -1);
    vector <int> min_next(n, n);
    stack <int> st;

    for (int i=0; i<n; ++i) {
        while (!st.empty() && nums[st.top()] > nums[i]) {
            st.pop();
        }
        if (!st.empty()) min_prev[i] = st.top();

        st.push(i);
    }

    while (!st.empty()) {
        st.pop();
    }

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && nums[st.top()] >= nums[i]) {
            st.pop();
        }
        if (!st.empty()) min_next[i] = st.top();

        st.push(i);
    }

    for (int i=0; i<n; ++i) {
        int leftCount = i - min_prev[i];
        int rightCount = min_next[i] - i;

        ans += (1LL * leftCount * rightCount) % MOD * (nums[i]) % MOD;

        ans %= MOD;
    }

    return ans;
}

int main() {
    vector <int> nums = {3, 1, 2, 5};

    // cout << sum_of_subarray_minimums_1(nums);
    
    cout << sum_of_subarray_minimums_2(nums);

    cout << endl;
    return 0;
}