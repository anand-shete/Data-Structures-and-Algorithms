#include <bits/stdc++.h>

using namespace std;
// Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.


// O(n), O(1)
int linear_search(vector <int> &nums, int target) {
    int n = nums.size();

    for (int i=0; i<n; ++i) {
        if (nums[i] == target) {
            return i;
        }
    }

    return -1;
}

int main() {
    vector <int> nums = {5,4,3,2,1};
    int target = 5;
    target = -5;

    cout << linear_search(nums, target) << endl;

    return 0;
}