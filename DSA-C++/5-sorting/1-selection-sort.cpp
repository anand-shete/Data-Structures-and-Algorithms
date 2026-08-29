#include <bits/stdc++.h>

using namespace std;

// Selection sort - O(n²) , O(1)
void selection_sort(vector <int> &arr) {
    // find and place min element in each iteration to correct place
    int size = arr.size();

    for (int i=0; i<size; i++) {
        int min = i;
        for (int j=i+1 ; j<size ;j++) {
            if (arr[j] < arr[min]) {
                min = j;
            }
        }
        swap(arr[i], arr[min]);
    }
}

int main() {
    vector <int> arr = {56,34,32,13,54,26,20,9};

    selection_sort(arr);

    for(auto x:arr) {
        cout << x << " ";
    } cout << endl;
    return 0;
}