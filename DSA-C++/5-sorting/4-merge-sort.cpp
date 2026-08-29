#include <bits/stdc++.h>

using namespace std;


// Merge sort - O(n.logn) , O(n)
void merge (vector <int> &arr, int low, int mid, int high) {
    vector <int> temp;
    int left = low;
    int right = mid +1;

    while (left <= mid && right <= high) {
        if(arr[left] > arr[right]) {
            temp.push_back(arr[right]);
            right++;
        } 
        else {
            temp.push_back(arr[left]);
            left++;
        }
    }

    // push leftover elements
    while (right <= high) {
        temp.push_back(arr[right]);
        right++;
    }

    while (left <= mid) {
        temp.push_back(arr[left]);
        left++;
    }

    // update original array
    for (auto i=low; i <= high; i++) {
        arr[i] = temp[i-low];
    }
}

void divide(vector <int> &arr, int low, int high) {
    if (low >= high) return;

    int mid = (low + high) / 2;

    divide(arr, mid+1, high);
    divide(arr, low, mid);

    merge(arr, low, mid, high);
}


int main() {
    vector <int> arr = {78,34,38,2,3,5,9};
    
    divide(arr, 0, arr.size() - 1);

    for (auto x:arr) cout << x << " "; 
    
    cout << endl;
    return 0;
}