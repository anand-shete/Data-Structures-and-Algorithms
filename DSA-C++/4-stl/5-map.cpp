#include <iostream>
#include <map>
#include <unordered_map>

using namespace std;
int main() {
    // A map is a data structure which stores unique keys

    // An ordered map stores these "unique keys" in SORTED order (numerically/alphabetically)
    // All operations take O(log n)
    
    map <int,int> omap = {{23,3} , {13,21} ,{13,9} , {2,35} , {5,28}};

    // If you access a non-existent value using [],
    // the key is created, with default value based on the value type of map
    cout << "key 3 has value of: " << omap[3] << endl;

    // count() return true if element with given key exists in map
    cout << "does 13 exists in omap: " << omap.count(13) << endl;

    // find() returns iterator pointed to element if it exists
    auto itr = omap.find(2);
    if (itr != omap.end()) {
        cout << "key "<< itr->first << " has a value: "<< itr->second << endl;
    }

    // insert() only if the key did not exist in map
    // returns pair<iterator, bool> where bool is true for successful insertions
    auto x = omap.insert({ 5, 8 });
    cout << "is key 5 inserted: " << x.second << endl;

    // delete key value pair
    cout << "delete pair with key 13: " << omap.erase(13) << endl;

    // first element >= given key can be found in ordered map
    auto lower = omap.lower_bound(5);
    if (lower != omap.end()) {
        cout << "key >= 5->" << lower->first << " val->" << lower->second << endl;
    }
 
    // first element > given key
    map <int,int>::iterator upper = omap.upper_bound(5);
    if (upper != omap.end()) {
        cout << "key > 5->" << upper->first << " val->" << upper->second << endl;
    }


    // size of map - O(1)
    cout << "size of map is: " << omap.size() << endl;

    // is map empty - O(1)
    cout << "is map empty: " << omap.empty() << endl;

    // tranversing a map - O(n)
    for (auto &[k,v]:omap) {
        cout << k << "->" << v << endl;
    }
    
    // clear a map - O(n)
    omap.clear();
    cout << "\n\n";
    
    
    
    
    
    
    
    
    // Hash map
    // An unordered map stores "unique keys" in random order
    // int, bool, char, string, long long are used as keys for DSA
    // Most operations have time complexty O(1) in average case and O(n) in absolute worst-case (hash collisions and poor hash functions)

    unordered_map <int,int> umap = {{2,20} , {5,50} , {8,'A'}};

    // If you access with [], the key is created based on value type of the map if it didn't existed
    umap[5] = 30;

    // insert without update
    cout << "insert key 2 in the map: " << umap.insert({2,100}).second << endl;

    // check if key exists
    cout << "is there pair which has key 5: " << umap.count(5) << endl;

    // find() returns an iterator pointed to given key if it exists
    auto it = umap.find(5);
    if (it != umap.end()) {
        cout << "key 2 has a value of: " << it -> second << endl;
    }

    // delete a key
    cout << "Delete key 10: " <<  umap.erase(10) << endl;

    // size of map
    cout << "Size of umap is " << umap.size() << endl;

    // check if map empty
    cout << "Is map empty: " << umap.empty() << endl;


    // traverse a map - O(n)
    for (auto it:umap) {
        cout << it.first << " -> " << it.second << endl; 
    }

    // delete a map - O(n)
    umap.clear();

    return 0;
}


// How do Unordered contatiners Work Internally?
// Hash Function: A hash function is applied to the key to compute a hash value. The hash value determines the bucket where the key-value pair is stored.
// Collision Handling: Hash collisions can occur when two keys map to the same bucket are handled using chaining. Chaining stores multiple key-value pairs in the same bucket as a linked list.
// Load Factor: The load factor is the ratio of the number of elements to the number of buckets. If the load factor exceeds a certain threshold, the container automatically resizes (rehashes) to maintain performance.
// unordered_map automatically grows and redistributes its buckets (rehashes) when the number of elements exceeds a certain threshold (load factor \(\approx 1.0\)) to keep collisions low.
