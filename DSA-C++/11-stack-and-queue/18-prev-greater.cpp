#include <bits/stdc++.h>

using namespace std;

// Q. Find the previous greater element for every element in array. Use -1 if no succh element exists.

// brute force - O(n²), O(1)
vector <int> prev_greater_1(vector <int> nums) {
    int n = nums.size();
    vector <int> ans;

    for (int i=0; i<n; ++i) {
        int prev_greater = -1;

        for (int j=0; j<i; ++j) {
            if (nums[j] > nums[i]) {
                prev_greater = nums[j];
                break;
            }
        }

        ans.push_back(prev_greater);
    }

    return ans;
}


// stack - O(n), O(n)
vector <int> prev_greater_2(vector <int> &nums) {
    int n = nums.size();
    vector <int> ans(n, -1);
    stack <int> st;

    for (int i=0; i<n; ++i) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            st.pop();
        }

        if (!st.empty()) {
            ans[i] = nums[st.top()];
        }

        st.push(i);
    }

    return ans;
}

int main() {
    vector <int> nums = {10, 20, 30, 15]};

    for (auto x:prev_greater_1(nums)) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}