#include <bits/stdc++.h>

using namespace std;
// Q. Range of a subarray of nums is the difference between the largest and smallest element in the subarray.
// For a given array, return the sum of all subarray ranges of nums.


// brute force - O(n²), O(1)
long long range_of_subarrays_1(vector <int> &nums) {
    long long ans = 0;
    int n = nums.size();

    for (int i=0; i<n; ++i) {
        int mini=INT_MAX, maxi=INT_MIN;

        for (int j=i; j<n; ++j) {
            if (nums[j] < mini) {
                mini = nums[j];
            }

            if (nums[j] > maxi) {
                maxi = nums[j];
            }

            ans += maxi-mini;
        }
    }

    return ans;
}

// stack - O(n), O(n)
long long range_of_subarrays_2(vector <int> &nums) {
    int n = nums.size();
    vector <int> maxPrev(n, -1), maxNext(n, n), minPrev(n, -1), minNext(n, n);
    stack <int> st;
    long long ans=0;

    for (int i=0; i<n; ++i) {
        while (!st.empty() && nums[st.top()] < nums[i]) {
            st.pop();
        }
        if (!st.empty()) {
            maxPrev[i] = st.top();
        }
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && nums[st.top()] <= nums[i]) {
            st.pop();
        }
        if (!st.empty()) {
            maxNext[i] = st.top();
        }
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i=0; i<n; ++i) {
        while (!st.empty() && nums[st.top()] > nums[i]) {
            st.pop();
        }
        if (!st.empty()) {
            minPrev[i] = st.top();
        }
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && nums[st.top()] >= nums[i]) {
            st.pop();
        }
        if (!st.empty()) {
            minNext[i] = st.top();
        }
        st.push(i);
    }

    for (int i=0; i<n; ++i) {
        long long leftMin = i-minPrev[i], leftMax = i-maxPrev[i], rightMin=minNext[i]-i, rightMax=maxNext[i]-i;

        ans += (leftMax * rightMax - leftMin * rightMin) * nums[i];
    }

    return ans;
}

// long long subArrayRanges(vector<int>& nums) {
//     int n = nums.size();
//     long long sum = 0;
//     stack<int> st;

//     // 1. Single Pass for ALL Minimums
//     for (int i = 0; i <= n; i++) {
//         // Use a dummy value (INT_MIN) at index n to force-pop everything remaining
//         long long curVal = (i == n) ? INT_MIN : nums[i]; 
        
//         while (!st.empty() && nums[st.top()] >= curVal) {
//             int mid = st.top();
//             st.pop();
//             long long leftBoundary = st.empty() ? -1 : st.top();
//             long long rightBoundary = i;
            
//             // Distance calculation
//             long long count = (mid - leftBoundary) * (rightBoundary - mid);
//             sum -= count * nums[mid]; // Subtract minimum contributions
//         }
//         st.push(i);
//     }

//     while (!st.empty()) st.pop(); // Clear stack for reuse

//     // 2. Single Pass for ALL Maximums
//     for (int i = 0; i <= n; i++) {
//         // Use a dummy value (INT_MAX) at index n to force-pop everything remaining
//         long long curVal = (i == n) ? INT_MAX : nums[i]; 
        
//         while (!st.empty() && nums[st.top()] <= curVal) {
//             int mid = st.top();
//             st.pop();
//             long long leftBoundary = st.empty() ? -1 : st.top();
//             long long rightBoundary = i;
            
//             // Distance calculation
//             long long count = (mid - leftBoundary) * (rightBoundary - mid);
//             sum += count * nums[mid]; // Add maximum contributions
//         }
//         st.push(i);
//     }

//     return sum;
// }

int main() {
    vector <int> nums = {4,-2,-3,4,1};

    // cout << range_of_subarrays_1(nums) << endl;

    cout << range_of_subarrays_2(nums) << endl;

    return 0;
}