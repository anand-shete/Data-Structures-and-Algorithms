#include <bits/stdc++.h>

using namespace std;

// Brute force - O(n²), O(1)
vector <int> leaders_in_array_1(vector <int> nums) {
    vector <int> ans;
    int n = nums.size();

    for (int i=0; i<n; ++i) {
        bool leader = true;

        for (int j=i+1; j<n; ++j) {
            if (nums[j] > nums[i]) {
                leader = false;
                break;
            }
        }

        if (leader) {
            ans.push_back(nums[i]);
        }
    }

    return ans;
}

// Optimal - o(n), O(n)
vector <int> leaders_in_array_2(vector <int> nums) {
    vector <int> ans;
    int n = nums.size(), max = INT_MIN;

    for (int i=n-1; i>=0; --i) {
        if (nums[i] >= max) {
            ans.push_back(nums[i]);
            max = nums[i];
        }
    }

    reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    vector <int> nums = {10, 22, 12, 3, 0, 6};
    // An element is a leader if its greater than all elements to its right
    // return all leaders of an array

    // for (int x:leaders_in_array_1(nums)) cout << x << " ";

    for (int x:leaders_in_array_2(nums)) cout << x << " ";

    cout << endl;
    return 0;
}