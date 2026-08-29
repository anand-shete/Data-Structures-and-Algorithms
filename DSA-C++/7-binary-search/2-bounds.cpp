#include <bits/stdc++.h>

using namespace std;

// O(log(n)), O(1)
int lower_bound (vector <int> &arr, int x) {
    // Lower bound is smallest index of array which has value >= x
    // Return size of array if no such element exists
    
    int low = 0, high = arr.size()-1;
    int ans = arr.size();
    
    while (low <= high) {
        int mid = (low + high)/2;

        if (arr[mid] < x) {
            low = mid+1;
        }

        else {
            ans = mid;
            high = mid-1;
        }
    }

    return ans;
}


// O(log(n)), O(1)
int upper_bound (vector <int> arr, int x) {
    // Upper bound is smallest index in sorted array having value > x
    // Return size of array if no such element exists

    int low = 0, high = arr.size()-1;
    int ans = arr.size();

    while (low <= high) {
        int mid = (low + high)/2;

        if (arr[mid] <= x) {
            low = mid+1;
        }

        else {
            ans = mid;
            high = mid-1;
        }
    }

    return ans;
}


int main() {
    vector <int> arr = {3, 4, 4, 7, 8, 10};
    int x = 2;

    cout << lower_bound(arr,x) << endl;
    cout << upper_bound(arr,x) << endl;
    
    return 0;
}