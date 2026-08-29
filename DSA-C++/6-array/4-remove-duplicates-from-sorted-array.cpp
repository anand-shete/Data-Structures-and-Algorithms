#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.


// Two pointers - O(n), O(1)
int remove_duplicates_from_sorted_array(vector <int> &nums) {
    int n = nums.size(), i=1;

    for (int j=1; j<n; ++j) {
        if (nums[i-1] != nums[j]) {
            nums[i] = nums[j];
            i++;
        }
    }

    return i;
}

int main() {
    vector <int> nums = {0,0,1,1,1,2,2,3,3,4};
    nums = {1,2,2,2,3,3,4};
    // nums = {1,1,2};

    int size = remove_duplicates_from_sorted_array(nums);

    for (int i=0; i<size; ++i) {
        cout << nums[i] << " ";
    }

    cout << endl;

    return 0;
}