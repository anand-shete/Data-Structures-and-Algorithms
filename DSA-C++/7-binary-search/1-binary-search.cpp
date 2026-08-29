#include <bits/stdc++.h>

using namespace std;

// O(log n), O(1)
int binary_search(vector <int> nums, int target) {
    int low = 0, high = nums.size()-1;

    while (low <= high) {
        int mid = low + (high-low) / 2;

        if (target > nums[mid]) {
            low = mid+1;
        }
        else if (target < nums[mid]) {
            high = mid-1;
        }
        else {
            return mid;
        }
    }
    return -1;
}

int main() {
    vector <int> nums = {3, 4, 5, 6, 7, 8, 9, 10};
    int target = 5;

    cout << binary_search(nums, target) << endl;
    
    return 0;
}