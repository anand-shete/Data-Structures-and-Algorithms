#include <bits/stdc++.h>

using namespace std;

// O(n²), O(n)
void recursive_insertion_sort(vector <int> &arr, int i, int n) {
    if (i == n) return;

    int j=i;
    while (j>0 && arr[j-1]>arr[j]) {
        swap(arr[j-1], arr[j]);
        j--;
    }

    recursive_insertion_sort(arr, i+1, n);
}

// O(n²), O(1)
void insertion_sort(vector <int> &arr) {
    // take an element, shift others right and insert element
    for (int i=1; i<arr.size(); i++) {
        int ele = arr[i];
        int j=i-1;

        while (j>=0 && arr[j]>ele) {
            arr[j+1] = arr[j];
            j--;
        }

        arr[j+1] = ele;        
    }
}


int main() {
    vector <int> arr = {56,34,32,13,54,26,20,9};

    // insertion_sort(arr);
    recursive_insertion_sort(arr, 0, arr.size());

    for(auto x:arr) {
        cout << x << " ";
    } cout << endl;
    
    return 0;
}