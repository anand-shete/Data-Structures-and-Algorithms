#include <bits/stdc++.h>

using namespace std;
// Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements. Note that you must do this in-place without making a copy of the array.


// brute force - O(n), O(n)
void move_zeroes_to_end_1(vector <int> &nums) {
    int n = nums.size();
    vector <int> temp;

    for (int &x:nums) {
        if (x != 0) {
            temp.push_back(x);
        }
    }

    for (int i=temp.size(); i<n; ++i) {
        temp.push_back(0);
    }

    for (int i=0; i<n; ++i) {
        nums[i] = temp[i];
    }
}


// Two pointers - O(n), O(1)
void move_zeroes_to_end_2(vector <int> &nums) {
    int n = nums.size();
    int j=0, i=0;

    while (i < n) {
        if (nums[i] != 0) {
            swap(nums[i], nums[j]);
            ++j;
        }
        ++i;
    }
}

int main() {
    vector <int> nums = {0,1,0,3,12};
    nums = {1,0,0,3,12};
    // nums = {0,0,1,3,12};

    // move_zeroes_to_end_1(nums);

    move_zeroes_to_end_2(nums);

    for (int &x:nums) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}