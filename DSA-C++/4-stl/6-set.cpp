#include <bits/stdc++.h>

using namespace std;

int main() {
    // A set data structure stores unique elements
    // An ordered set stores unique elements in a SORTED order (numerically/alphabetically)
    // Most operation take O(log n)

    set <int> oset = {5,1,0,0,6,6};

    vector <int> arr = {1,2,3,3,3,4};
    set <int> osetFromArr(arr.begin(), arr.end());
    
    // check if element exists
    cout << "does 5 exist in set: " << oset.count(5) << endl;

    // safe insert
    cout << "is 6 inserted: " << oset.insert(6).second << endl;

    // delete element
    cout << "is 3 removed: " << oset.erase(3) << endl;

    // size of set – O(1)
    cout << "Size of set is: " << oset.size() << endl;

    // check if empty - O(1)
    cout << "Is set empty: " << oset.empty() << endl;

    // traverse a set - O(n)
    for (auto &x:oset) {
        cout << x << " ";
    }   cout << endl;

    // delete entire set - O(n)
    oset.clear();

    // Upper bound
    auto ub = osetFromArr.upper_bound(99);
    if (ub != osetFromArr.end()) {
        cout << "first element > 3: " << *ub << endl;
    }
    
    // lower bound
    auto lb = osetFromArr.lower_bound(3);
    if (lb != osetFromArr.end()) {
        cout << "first element >= 3: " << *lb << endl;
    }
    
    cout << "\n\n\n";
    
    
    



    // Hash set
    // An unordered set stores unique elements in random order
    // All operations take O(1) time complexity in the average case and O(n) in absolute worst case (hash collisions)

    unordered_set <int> uset = {3,4,5,5,6,7};

    // Insert elements
    uset.insert(5);
    uset.insert(2);

    // Check if element exists
    cout << "\n5 exists in hash set: " << uset.count(5);

    // Remove elements
    cout << "\nis 3 deleted from hash set: " << uset.erase(3);

    // size of hash set
    cout << "\nsize of hash set: " << uset.size();

    // check if empty
    cout << "\nis hash set empty: " << uset.empty();

    // Traverse set - O(n)
    for (auto &x:uset) {
        cout << x << " ";
    }

    // Delete entire set - O(n)
    uset.clear();

    return 0;
}








/*  
    // Unordered contatiners
    In C++, std::unordered_map is the go-to choice for implementing hash maps. It is efficient, flexible, and highly useful in scenarios where quick lookups and insertions are needed.
    std::unordered_map is a container that stores key-value pairs, where keys are unique, and each key is associated with a value. It uses a hashing mechanism to map keys to values, providing average O(1) time complexity for insertion, deletion, and lookup operations.
    The choice between std::unordered_map and std::map depends on whether we need order (std::map) or speed (std::unordered_map)
    Key-Value Pair Storage: Each element in the map is a pair: std::pair<const Key, Value>.
    Hashing: Keys are hashed to determine their storage location.
    No Order Guarantee: The elements are not stored in any specific order.
    Fast Access: Average time complexity for most operations is O(1).
    Custom Hash Functions: We can define custom hash functions for complex keys.

    How Does It Work Internally?
    Hash Function: A hash function is applied to the key to compute a hash value. The hash value determines the bucket where the key-value pair is stored.
    Collision Handling: Hash collisions (when two keys map to the same bucket) are handled using chaining. Chaining stores multiple key-value pairs in the same bucket as a linked list.
    Load Factor: The load factor is the ratio of the number of elements to the number of buckets. If the load factor exceeds a certain threshold, the container automatically resizes (rehashes) to maintain performance.
    
    // Functions Specific to std::unordered_map
    std::unordered_map has hash table-specific functions:
    bucket_count()
    bucket_size()
    bucket()
    load_factor()
    max_load_factor()
    rehash()
    reserve()

    // Other functions of unordered_set 
    cbegin() – it refers to the first element of the unordered set.
    cend() – it refers to the theoretical element after the last element of the unordered set.
    bucket_size() - gives the total number of elements present in a specific bucket in an unordered set.
    emplace() - to insert an element in the unordered set.
    max_size() - the maximum elements an unordered_set can hold.
    max_bucket_count() - to check the maximum number of buckets an unordered set can hold.
*/