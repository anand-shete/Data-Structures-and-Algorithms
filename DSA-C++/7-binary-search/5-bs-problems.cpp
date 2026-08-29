#include <bits/stdc++.h>

using namespace std;

// Linear search - O(n), O(1)
int rotated_array_1(vector <int> arr) {
    // given array from 1 to n rotated n times, return n
    int min = 0;

    for (int i=0 ; i<arr.size(); i++) {
        if (arr[i] > arr[i+1]) {
            return i+1;
        }
    }

    return -1;
}

// Binary search - O(log(n)), O(1)
int find_how_many_times_array_rotated_2 (vector <int> arr) {
    int low = 0, high = arr.size()-1;

    while (low < high) {
        int mid = (low + high)/2;

        if (arr[mid] < arr[high]) {
            high = mid;
        }
        else {
            low = mid + 1;
        }
    }

    return low;
}

int main() {
    vector <int> arr = {3, 4, 4, 7, 8, 10};

    // cout << rotated_array_1(arr);  
    cout << rotated_array_2(arr);

    cout << endl;
    return 0;
}