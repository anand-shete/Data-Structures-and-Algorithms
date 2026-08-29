#include <bits/stdc++.h>

using namespace std;

// O(n²), O(n)
void recursive_bubble_sort(vector <int> &arr, int n) {
    if (n == 1) return;

    for (int i=0; i<n-1; i++) {
        if (arr[i] > arr[i+1]) {
            swap(arr[i], arr[i+1]);
        }
    }

    recursive_bubble_sort(arr, n-1);
}


// O(n²), O(1)
void bubble_sort(vector <int> &arr) {
    // bubbles next largest value to last
    int n = arr.size();

    for (int i=1; i<n ; i++) {
        for (int j=0 ; j<n-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(arr[j] , arr[j+1]);
            }
        }
    }
}


int main() {
    vector <int> arr = {56,34,32,13,54,26,20,9};

    recursive_bubble_sort(arr, arr.size());
    // bubble_sort(arr);

    for(auto x:arr) {
        cout << x << " ";
    } cout << endl;

    return 0;
}