#include <bits/stdc++.h>

using namespace std;


// Space complexity - O(1)
// Worst case time complexity - O(n²)
// Avg. case time complexity - O(n. log n)
// Best case time complexity - O(n. log n)
int partition(vector <int> &arr, int low, int high) {
    int pivot = arr[low];
    int left = low;
    int right = high;

    // place elements relative to pivot (<= on one side, > on other)
    while (left < right) {
        while (arr[left] <= pivot && left < high) {
            left++;
        }

        while (arr[right] > pivot) {
            right--;
        }

        if (left < right) {
            swap(arr[left], arr[right]); 
        }
    }

    // place pivot at correct position
    swap(arr[low], arr[right]);

    return right;
}

void quick_sort (vector <int> &arr, int low, int high) {
    if (low >= high) return;
    
    int boundaryIdx = partition(arr, low, high);

    quick_sort(arr, low, boundaryIdx-1);
    quick_sort(arr, boundaryIdx+1, high);
}

int main() {
    vector <int> arr = {34,12,2,6,24,43};
    
    quick_sort(arr, 0, arr.size() - 1);

    for (auto x:arr) cout << x << " "; 
    
    cout << endl;
    return 0;    
}