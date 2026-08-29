#include <bits/stdc++.h>

using namespace std;
// Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
// We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.



// brute force - O(n), O(1)
void sort_0_1_and_2_approach1(vector <int> &nums) {
    int n = nums.size(), cnt0, cnt1, cnt2;
    cnt0 = cnt1 = cnt2 = 0;

    for (int &x:nums) {
        if (x == 0) {
            cnt0++;
        }
        else if (x == 1) {
            cnt1++;
        }
        else {
            cnt2++;
        }
    }

    int i=n;
    while (cnt2--) {
        nums[--i] = 2;
    }

    while (cnt1--) {
        nums[--i] = 1;
    }

    while (cnt0--) {
        nums[--i] = 0;
    }
}


// dutch national flag - O(n), O(1)
void sort_0_1_and_2_approach2 (vector <int> &nums) {
    int n = nums.size();
    int low=0, mid=0, high=n-1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            ++low;
            ++mid;
        }
        else if (nums[mid] == 1) {
            ++mid;
        }
        else {
            swap(nums[mid], nums[high]);
            --high;
        }
    }
}

int main() {
    vector <int> nums = {1,0,2,1,0};
    nums = {2,0,2,1,1,0};
    // nums = {0,2,0,2,2};
    // nums = {2,2,1,1,0,0};
    // nums = {};


    // sort_0_1_and_2_approach1(nums);

    sort_0_1_and_2_approach2(nums);

    for (int &x:nums) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}