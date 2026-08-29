#include <bits/stdc++.h>

using namespace std;

// Q. Given circular integer array, return next greater element of array, -1 if it does not exists

// brute force - O(n²), O(1)
vector <int> next_greater_element_1(vector <int> nums) {
    int n = nums.size();
    vector <int> ans(n, -1);

    for (int i=0; i<n; ++i) {
        int curr = nums[i];

        for (int j=0; j<n; ++j) {
            int idx = (i+j) % n;

            if (nums[idx] > curr) {
                ans[i] = nums[idx];
                break;
            }
        }
    }

    return ans;
}

// stack - O(n), O(n)
vector <int> next_greater_element_2(vector <int> nums) {
    int n=nums.size();
    vector <int> ans(n, -1);
    stack <int> st;

    for (int i=2*n-1; i>=0; --i) {
        int curr = nums[i%n];

        while (!st.empty() && st.top()<=curr) {
            st.pop();
        }

        if (!st.empty() && i<n) {
            ans[i] = st.top();
        }
        
        st.push(nums[i%n]);
    }

    return ans;
}

int main() {
    vector <int> nums = {3, 10, 4, 2, 1, 2, 6, 1, 7, 2, 9};

    // vector <int> ans = next_greater_element_1(nums);

    vector <int> ans = next_greater_element_2(nums);

    for (int x:ans) cout << x << " ";

    cout << endl;
    return 0;
}