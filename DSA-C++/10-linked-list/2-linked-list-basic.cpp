#include <bits/stdc++.h>

using namespace std;

// Elements are not store at contigious memory locations
struct Node {
    int data;           // data
    Node* next;         // pointer to next node

    Node(int x, Node* next): data(x), next(ptr) {}
    Node(int x): data(x),next(nullptr) {}
};


int main() {
    Node* node = new Node(10);      // this is a node
    Node* ptr = node;               // copies memory address of a node, stored in stack memory, no cleanup required

    cout << "data part stored in heap: " << node->data << endl;
    cout << "address of next node stored in heap: " << node->next << endl;   

    cout << "address of current node stored in stack: " << node << endl;

    cout << "ptr to current node stores copied address in stack: " << ptr << endl;

    // segmentation fault is triggered when program tries to access invalid memory location
    // cout << node->next->data ;
    return 0;
}