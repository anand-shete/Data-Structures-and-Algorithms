#include <bits/stdc++.h>

using namespace std;
// Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

// Implement the LRUCache class:

// LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
// int get(int key): Return the value of the key if the key exists, otherwise return -1.
// void put(int key, int value): Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

// The functions get and put must each run in O(1) average time complexity.


// O(1), O(capacity)
struct LRUCache {
    struct Node;
    int cap;
    unordered_map <int, Node*> umap;
    Node* head;
    Node* tail;

    struct Node {
        int key, val;
        Node* next;
        Node* prev;
        
        Node(int _key, int _val): key(_key), val(_val) {};
    };

    LRUCache(int _cap) {
        cap = _cap;
        head = new Node(-1, -1);
        tail = new Node(-1, -1);

        head->next = tail;
        tail->prev = head;
    }

    ~LRUCache() {
        Node* curr = head;
        while (curr != tail) {
            Node* nextNode = curr->next;
            delete curr;

            curr = nextNode;
        }
    
        delete curr;
    }

    void addNode(Node* node) {
        Node* temp = head->next;

        node->prev = head;
        head->next = node;

        node->next = temp;
        temp->prev = node;
    }

    void delNode(Node* node) {
        node->prev->next = node->next;
        node->next->prev = node->prev;
    }

    int get(int _key) {
        if (!umap.count(_key)) {
            return -1;
        }
        
        Node* node = umap[_key];
        int val = node->val;

        // move node to front
        delNode(node);
        addNode(node);

        return val;
    }

    void put(int _key, int _val) {
        if (umap.count(_key)) {
            Node* temp = umap[_key];
            temp->val = _val;
            delNode(temp);
            addNode(temp);
            return;
        }

        if (umap.size() == cap) {
            Node* temp = tail->prev;
            int key = temp->key;
            delNode(temp);
            delete temp;
            umap.erase(key);
        }

        Node* add = new Node(_key, _val);
        umap[_key] = add;

        addNode(add);
    }
};

int main() {
    LRUCache lru(2);

    lru.put(1, 1); // cache is {1=1}
    lru.put(2, 2); // cache is {1=1, 2=2}

    cout << lru.get(1) << endl;    // return 1

    lru.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}

    cout << lru.get(2) << endl;    // returns -1 (not found)

    lru.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}

    cout << lru.get(1) << endl;    // return -1 (not found)
    cout << lru.get(3) << endl;    // return 3
    cout << lru.get(4) << endl;    // return 4

    return 0;
}