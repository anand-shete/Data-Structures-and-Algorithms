#include <iostream>
#include <array>
#include <vector>

using namespace std;
int main() {
    // vectors are dynamic arrays.
    // Most operations of vector take constant time O(1)
    
    
    // Initialization
    // vector <type> name;
    vector <int> vec1;                  // empty vector of type int 
    vector <int> vec2(5);               // 5 elements value-initialized to 0 (size=5)
    vector <int> vec3(5, 10);           // 5 elements initialized to 10
    vector <int> vec4 = {1,2,3,4};      // 4 elements initialized with given values
    vector <int> vec5(vec4);            // copied initialization from vec4
    // for (auto x:vec5) cout << x << " ";cout << "\n";


    // First and last element
    cout << "\nfirst element: " << vec4.front();
    cout << "\nlast element: " << vec4.back();

    // Accessing using indices
    cout << "\nat() introduces overhead due to bounds checking: " << vec4.at(2);
    cout << "\nfor quick access: " << vec4[2];

    // size of vector
    cout << "\nsize of vec4: " << vec4.size();

    // capacity() returns total number of elements the vector can hold without reallocating memory 
    cout << "\ncapacity of vec4: " << vec4.capacity();

    // empty() returns true if vector is empty
    cout << "\nis vec4 empty: " << vec4.empty() <<endl;

    // erase an element in range of iterator [start, end)
    for (int x:vec4) cout << x << " "; cout << endl;
    vec4.erase(vec4.begin());                           // delete 1st element
    vec4.erase(vec4.begin()+1, vec4.begin()+3);         // delete from index 1 to 2
    for (int x:vec4) cout << x << " "; cout << endl;

    // push_back is an ammortized O(1) operation
    // means it takes O(1), but can take O(n) if the vector has reached its capacity (due to reallocation)
    vec4.push_back(3);
    cout << "\nsize of vec4 after push_back: " << vec4.size();

    // remove last element of the vector
    vec4.pop_back();


    // The following operations have a linear time complexity - O(n)
    // arr.begin() returns an iterator that points to the first element in the array.
    // arr.end() returns an iterator points to theoretical element after the last element.
    cout << "\niterator based for loop: ";
    for(auto i=vec5.begin() ; i < vec5.end() ; i++) {
        cout << *i << " ";
    }

    // under the hood, range based for loop is compiled into an iterator based for loop
    cout << "\nrange based for loop: ";
    for(auto x:vec5) {
        cout << x << " ";
    }

    // Resizing vector
    vec1.resize(10);
    vec2.resize(10, 4);

    // clear() function removes all elements from vector, keeping capacity same
    vec2.clear();
    cout << "\ncapacity of vec2: " << vec2.capacity();
    cout << "\nsize of vec2: " << vec2.size();

    // you can reserve space in memory if you know the no. of elements you will store
    vec1.reserve(50);
    cout << "\ncapacity of vec1: " << vec1.capacity();

    // shrink_to_fit() reduces the capacity to match the size
    vec1.shrink_to_fit();
    cout << "\ncapacity of vec1: " << vec1.capacity();

    cout << endl;
}