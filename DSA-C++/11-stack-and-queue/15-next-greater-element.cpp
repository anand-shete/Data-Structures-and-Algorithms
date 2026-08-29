#include <bits/stdc++.h>

using namespace std;

// Q. Given an array, replace every element with its next greater element, -1 if it does not exists

// stack - O(n), O(n)
vector <int> next_greater_element(vector <int> nums) {
    int n = nums.size();
    vector <int> ans(n, -1);
    stack <int> st;

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && nums[st.top()] <= nums[i]) {
            st.pop();
        }

        if (!st.empty()) ans[i] = nums[st.top()];

        st.push(i);
    }

    return ans;
}

int main() {
    vector <int> nums = {1, 3, 2, 4};
    nums = {6, 8, 0, 0, 0, 1, 1, 3};

    vector <int> ans = next_greater_element(nums);

    for (int x:ans) cout << x << " ";

    cout << endl;
    return 0;
}