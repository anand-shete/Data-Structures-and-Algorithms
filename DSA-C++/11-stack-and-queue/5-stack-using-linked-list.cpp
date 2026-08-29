#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode* next;

    ListNode(int x, ListNode* ptr): val(x), next(ptr) {}
    ListNode(int x): val(x) {}
};

// O(1), O(1)
class LinkedListStack {
ListNode* head;
int size;

public:
    LinkedListStack() {
        head = nullptr;
        size = 0;
    }

    void push(int x) {
        ListNode* node = new ListNode(x, head);
        head = node;

        size++;
    }

    int pop() {
        if (head == nullptr) {
            throw runtime_error("Stack is Empty");
        }
        int top = head->val;

        ListNode* temp = head;
        head = head->next;
        delete temp;

        size--;
        return top;
    }

    int top() {
        return head->val;
    }

    bool empty() {
        return size==0;
    }
};

int main() {
    LinkedListStack st;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    while (st.empty() != 1) {
        cout << st.top() << endl;
        st.pop();
    }

    return 0;
}