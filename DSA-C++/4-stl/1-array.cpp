#include <iostream>
#include <bits/stdc++.h>// sufficient for most dsa questions.

using namespace std;

void printArr(int* arr, int size) {
    for (int i=0; i<size; i++) {
        cout << arr[i] << " ";
    } cout << endl;
}

int main() {
    int arr1[5];                            // declare and initialize with garbage values
    int arr2[5] = {10};                     // declare and initialize entire array with 10
    int arr3[5] = {10, 20, 30, 40, '1'};    // declare and initialize with fixed values
    char arr4[5] = {'a', 'b', 'c'};         // character array

    // Accessing elements
    cout << arr1[2] << endl; 

    

    // When arrays are passed to a function, it "decays" into a pointer to its first element.
    // array is passed by reference
    printArr(arr3 , sizeof(arr3)/sizeof(int));


    
    // Multidimensional Arrays
    int arr2D[3][2] = { {1,2}, {3,4}, {5,6} };       // { 0th row, 1st row, 2nd row }
    cout << "2nd row 2nd element: " << arr2D[1][1] << endl << endl;

    return 0;
}


// Array Limitations
// Fixed Size
// No Bounds Checking
// Memory management