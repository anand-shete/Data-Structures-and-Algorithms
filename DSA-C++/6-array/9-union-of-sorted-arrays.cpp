#include <bits/stdc++.h>

using namespace std;
// Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.
// The union of two arrays can be defined as the common and distinct elements in the two arrays.
// NOTE: Elements in the union should be in ascending order.



// Ordered set - O(n.logn) , O(n) 
vector <int> union_of_sorted_arrays_1(vector <int> &nums1, vector <int> &nums2) {
    set <int> set(nums1.begin(), nums1.end());
    vector <int> temp;

    for (auto x:nums2) {
        set.insert(x);
    }

    int i=0;
    for (auto x:set) {
        temp.push_back(x);
    }

    return temp;
}

// Two pointers approach - O(n) , O(n)
vector <int> union_of_sorted_arrays_2(vector <int> &arr1, vector <int> &arr2) {
    int l1=0 , l2=0;
    vector <int> temp;

    while (l1 < arr1.size() && l2 < arr2.size()) {
        if (arr1[l1] < arr2[l2]) {
            if (temp.empty() || temp.back() != arr1[l1]) {
                temp.push_back(arr1[l1]);
            }
            l1++;
        }

        else if (arr1[l1] > arr2[l2]) {
            if (temp.empty() || temp.back() != arr2[l2]) {
                temp.push_back(arr2[l2]);
            }

            l2++;
        }

        else {
            if (temp.empty() || temp.back() != arr1[l1]) {
                temp.push_back(arr1[l1]);
            }
            l1++;
            l2++;
        }
    }

    while (l1 < arr1.size()) {
        if (temp.empty() || temp.back() != arr1[l1]) {
            temp.push_back(arr1[l1]);
        }
        l1++;
    }

    while (l2 < arr2.size()) {
        if (temp.empty() || temp.back() != arr2[l2]) {
            temp.push_back(arr2[l2]);
        }

        l2++;
    }

    return temp;
}


int main() {
    vector <int> arr1 = {1,2,3,4,5,6,7};
    vector <int> arr2 = {-1,-100,3,99};

    vector <int> ans = union_of_sorted_arrays_1(arr1,arr2);

    // vector <int> ans = union_of_sorted_arrays_2(arr1,arr2);

    for (auto x:ans) {
        cout << x << " ";
    }

    cout << endl;
    return 0;
}