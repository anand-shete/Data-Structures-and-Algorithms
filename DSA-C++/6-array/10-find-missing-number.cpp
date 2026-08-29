#include <bits/stdc++.h>

using namespace std;
// Given an array of size n-1 with distinct integers in the range of [1, n]. This array represents a permutation of the integers from 1 to n with one element missing. Find the missing element in the array.


// brute force - O(n²), O(1)
int missing_number_1(vector <int> &nums) {
    int n = nums.size();

    for (int i=1; i<=n; ++i) {
        bool present = false;

        for (int j=0; j<n; ++j) {
            if (nums[j] == i) {
                present = true;
                break;
            }
        }

        if (!present) {
            return i;
        }
    }

    return n+1;
}


// hashing - O(n), O(n)
int missing_number_2(vector <int> &nums) {
    int n = nums.size();
    unordered_set <int> uset;

    for (int &x:nums) {
        uset.insert(x);
    }

    for (int i=1; i<=n;++i) {
        if (!uset.count(i)) {
            return i;
        }
    }

    return n+1;
}


// sum difference - O(n), O(1)
int missing_number_3(vector <int> &nums) {
    int n = nums.size();
    long long sum2 = (1LL * (n+1) * (n+2)) / 2, sum1=0;

    for (int &x:nums) {
        sum1 += 1LL * x;
    }

    return sum2 - sum1;
}


// xor - O(n), O(1)
int missing_number_4(vector <int> &nums) {
    int n = nums.size() + 1;
    int xor_n = 0, xor_arr = 0;

    for (int &x:nums) {
        xor_arr ^= x;
    }

    for (int i=0; i<=n; ++i) {
        xor_n ^= i;
    }

    return xor_n ^ xor_arr;
}


int main() {
    vector <int> nums = {8, 2, 4, 5, 3, 7, 1};
    nums = {5,1,4,2};
    // nums = {2};

    cout << missing_number_1(nums) << endl;

    cout << missing_number_2(nums) << endl;

    cout << missing_number_3(nums) << endl;

    cout << missing_number_4(nums) << endl;
    
    return 0;
}