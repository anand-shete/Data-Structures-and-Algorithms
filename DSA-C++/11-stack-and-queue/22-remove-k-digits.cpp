#include <bits/stdc++.h>

using namespace std;

// Q. Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.



// stack - O(n), O(n)
string remove_k_digits(string nums, int k) {
    string ans = "";
    stack <int> st;

    if (k == 0) return nums;

    for (char c:nums) {
        while (!st.empty() && k>0 && st.top()>c) {
            st.pop();
            k--;
        }

        st.push(c);
    }

    while (!st.empty() && k>0) {
        st.pop();
        k--;
    }

    if (st.empty()) return "0";

    while (!st.empty()) {
        ans += st.top();
        st.pop();
    }

    while (!ans.empty() && ans.back()=='0') {
        ans.pop_back();
    }

    if (ans.empty()) return "0";

    reverse(ans.begin(), ans.end());

    return ans;
}

int main() {
    string nums = "1002991";
    int k = 3;
    nums = "1432219", k=3;
    nums = "10200", k=1;

    cout << remove_k_digits(nums, k) << endl;

    return 0;
}