#include <bits/stdc++.h>

using namespace std;
// Given an array, return the largest element in the array.



// sort - O(n. logn), O(1)
int largest_element_1(vector <int> &nums) {
    sort(nums.begin(), nums.end());

    return nums[nums.size()-1];
}

// optimal - O(n), O(1)
int largest_element_2(vector <int> &nums) {
    int ans = nums[0];

    for (int &x:nums) {
        if (x > ans) {
            ans = x;
        }
    }

    return ans;
}

int main() {
    vector <int> nums = {8, 10, 5, 7, 9};
    nums = {2, 5, 1, 3, 0};

    cout << largest_element_1(nums) << endl;

    cout << largest_element_2(nums) << endl;

    return 0;
}