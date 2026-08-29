#include <bits/stdc++.h>

using namespace std;
// Q. Find the next minimum element for every element of given array, -1 if not found and return new array.

// brute force - O(n²), O(1)
vector <int> next_smaller_1(vector <int> nums) {
    int n = nums.size();
    vector <int> ans(n, -1);

    for (int i=0; i<n; ++i) {
        for (int j=i+1; j<n; ++j) {
            if (nums[j] < nums[i]) {
                ans[i] = nums[j];
                break;
            }
        }
    }

    return ans;
}


// Stack - O(n), O(n)
vector <int> next_smaller_2(vector <int> nums) {
    int n = nums.size();
    vector <int> next_smaller(n, -1);
    stack <int> st;

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && nums[st.top()] >= nums[i]) {
            st.pop();
        }

        if (!st.empty()) next_smaller[i] = nums[st.top()];

        st.push(i);
    }

    return next_smaller;
}

int main() {
    vector <int> nums = {4, 8, 5, 5, 5, 2, 2, 25};

    // for (int x:next_smaller_1(nums)) cout << x << " ";
    
    for (int x:next_smaller_2(nums)) cout << x << " ";

    cout << endl;
    return 0;
}