#include <bits/stdc++.h>

using namespace std;

// O(1), O(1)
struct Node {
    int data;
    Node* next;

    Node (int x, Node* ptr) : data(x), next(ptr) {}
    Node (int x) : data(x), next(nullptr) {}
};


// O(n), O(1)
void print (Node* head) {
    while (head) {
        cout << head->data << " ";
        head = head->next;
    }
    cout << endl;
}


// O(n), O(n)
Node* array_to_ll(const vector <int> &arr) {
    if (arr.empty()) {
        return nullptr;
    }

    Node* head = new Node(arr[0]);
    Node* mover = head;
    
    for (int i=1; i<arr.size(); i++) {
        Node* temp = new Node(arr[i]);
        mover->next = temp;
        mover = mover->next;
    }

    return head;
}


// O(n), O(1)
bool search_in_ll(Node* head, int target) {
    while (head != nullptr) {
        if (head->data == target) {
            return true;
        }

        head = head->next;
    }

    return false;
}


// O(1), O(1)
Node* insert_at_head(Node* head, int x) {
    Node* node = new Node(x, head);

    return node;
}


// O(n), O(1)
Node* insert_at_tail(Node* head, int x) {
    if (head==nullptr) {
        return new Node(x);
    }

    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }

    Node* insert = new Node(x);
    temp->next = insert;

    return head;
}


// O(1), O(1)
Node* delete_head(Node* head) {
    if (head == nullptr) {
        return head;
    }

    Node* newHead = head->next;
    
    Node* delNode = head;
    delete delNode;

    return newHead;
}


// O(n), O(1)
Node* delete_tail(Node* head) {
    if (head==nullptr || head->next==nullptr) {
        return nullptr;
    }

    Node* temp = head;
    while (temp->next->next != nullptr) {
        temp = temp->next;
    }

    Node* endNode = temp->next;
    temp->next = nullptr;

    delete endNode;
    return head;
}


int main() {    
    vector <int> nums = {67,45,34,10};

    Node* head = array_to_ll(nums);

    // cout << search_in_ll(head, 10) << endl;

    // Node* node = insert_at_head(head, 3);

    // Node* node = insert_at_tail(head, 3);

    // Node* node = delete_head(head);

    // Node* node = delete_tail(head);
    

    print(node);

    return 0;
}