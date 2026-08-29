#include <bits/stdc++.h>

using namespace std;

// 
struct ListNode {
    int val;
    ListNode* next;

    ListNode(int data, ListNode* ptr): val(data), next(ptr) {}
    ListNode(int data): val(data) {}
};

class LinkedListQueue {
    ListNode* start;
    ListNode* end;
    int size;

public:
    LinkedListQueue() {
        start = end = nullptr;
        size = 0;
    }

    void push(int x) {
        ListNode* node = new ListNode(x);

        if (end == nullptr) {
            start = end = node;
        }
        else {
            end->next = node;
            end = node;
        }
        size++;
    }

    int pop() {
        if (size == 0) {
            throw runtime_error("Queue is empty");
        }

        int front = start->val;
        ListNode* delNode = start;
        start = start->next;

        delete delNode;
        size--;

        return front;
    }

    int peek() {
        if (size == 0) {
            throw runtime_error("Queue is empty");
        }

        return start->val;
    }

    bool empty() {
        return size==0;
    }
};


int main() {
    LinkedListQueue q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);

    while (q.empty() != 1) {
        cout << q.peek() << " ";
        q.pop();
    }

    cout << endl;
    return 0;
}