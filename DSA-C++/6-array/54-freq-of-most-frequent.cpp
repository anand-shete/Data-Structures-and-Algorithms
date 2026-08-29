#include <bits/stdc++.h>

using namespace std;

// sliding window - O(n.log n), O(log n)
vector <int> freq_of_most_freq_1(vector <int> nums, int k) {
    int left=0, n=nums.size(), maxFreq=0;
    long long sum = 0;

    sort(nums.begin(), nums.end());

    for (int right=left; right<n; ++right) {
        sum += nums[right];

        while (sum + k < 1LL * nums[right] * (right-left+1)) {
            sum -= nums[left];
            left++;
        }

        maxFreq = max(maxFreq, right-left+1);
    }

    return maxFreq;
}

int main() {
    vector <int> nums = {1,2,4};
    int k = 5;

    vector <int> ans = freq_of_most_freq_1(nums, k);

    for (int x:ans) cout << x << " ";

    cout << endl;
    return 0;
}