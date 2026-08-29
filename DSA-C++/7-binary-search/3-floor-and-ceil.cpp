#include <bits/stdc++.h>

using namespace std;

// O(log(n)), O(1)
int floor_in_array (vector <int> &arr , int x) {
    int low = 0, high = arr.size() - 1;
    int floor = 0;

    while (low <= high) {
        int mid = (low + high)/2;

        if (arr[mid] <= x) {
            floor = arr[mid];
            low = mid + 1;
        }

        else {
            high = mid - 1;
        }
    }
    
    return floor;
}


int ceil_of_array (vector <int> &arr, int x) {
    int low = 0, high = arr.size() -1;
    int ceil = -1;

    while (low <= high) {
        int mid = (low + high)/2;

        if (arr[mid] > x) {
            ceil = arr[mid];
            high = mid - 1;
        }

        else {
            low = mid + 1;
        }
    }

    return ceil;
}

int main() {
    vector <int> arr = {3, 4, 4, 7, 8, 10};
    int x = 5;

    cout << floor_in_array(arr, x) << endl;
    cout << ceil_of_array(arr, x) << endl;
    
    return 0;
}