#include <bits/stdc++.h>

using namespace std;
// Given an array, return the second smallest and second largest element in the array. -1 if none exists


// sort - O(n.logn), O(1)
pair <int, int> second_largest_and_second_smallest_1(vector <int> &nums) {
    int second_min = -1, second_max = -1;
    int n = nums.size();

    sort(nums.begin(), nums.end());

    if (n < 2) {
        return {second_min, second_max};
    }

    int min = nums[0], max = nums[n-1];
    for (int i=1; i<n; ++i) {
        if (nums[i] != min) {
            second_min = nums[i];
            break;
        }
    }

    for (int i=n-2; i>=0; --i) {
        if (nums[i] != max) {
            second_max = nums[i];
            break;
        }
    }

    return {second_min, second_max};
}


// optimal - O(n), O(1)
pair <int, int> second_largest_and_second_smallest_2(vector <int> &nums) {
    int n = nums.size();
    int max, second_max, min, second_min;
    max = second_max = INT_MIN, min = second_min = INT_MAX;

    for (int &x:nums) {
        if (x < min) {
            second_min = min;
            min = x;
        }
        else if (x < second_min && x != min) {
            second_min = x;
        }

        if (x > max) {
            second_max = max;
            max = x;
        }
        else if (x > second_max && x != max) {
            second_max = x;
        }
    }

    if (second_min == INT_MAX || second_max == INT_MIN) {
        second_min = second_max = -1;
    }

    return {second_min, second_max};
}


int main() {
    vector <int> nums = {1, 2, 4, 1, 7, 7, 5};
    // nums = {5, 5, 5, 5};
    // nums = {};
    // nums = {4};

    // pair <int, int> p = second_largest_and_second_smallest_1(nums);

    pair <int, int> p = second_largest_and_second_smallest_2(nums);

    cout << p.first << " " << p.second << endl;


    return 0;
}