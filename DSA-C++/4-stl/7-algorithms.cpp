#include <bits/stdc++.h>
#include <algorithm>

using namespace std;

int main() {
    vector <int> vec = {3, 10, 8, 6, 5};

    // Binary search - O(log n)
    cout << "6 present in vector: " << binary_search(vec.begin(), vec.end(), 6) << endl;


    // Introsort - 0(n logn)
    sort(vec.begin() , vec.end());
    cout << "after sort: ";
    for(auto x:vec) cout << x <<" "; cout << endl;


    // Rotate vector - O(n)
    // rotate (begin , new 0th index , end)
    rotate(vec.begin() , vec.begin() + 2 , vec.end());
    cout << "after rotating: " ;
    for(auto x:vec) cout << x <<" "; cout << endl;


    return 0;
}