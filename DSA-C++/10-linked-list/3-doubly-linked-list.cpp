#include <bits/stdc++.h>

using namespace std;

// O(1), O(1)
struct Node {
    int val;
    Node* prev;
    Node* next;

    Node (int x, Node* pre, Node* nex) : val(x), prev(pre), next(nex) {};
    Node (int x) : val(x), prev(nullptr), next(nullptr) {}
};

// O(n), O(1)
void printDLL (Node* head) {
    while (head != nullptr) {
        cout << head->val << " ";
        head = head->next;
    }

    cout << endl;
}

// O(n), O(1)
Node* arrayToDLL(vector <int> arr) {
    Node* head = new Node(arr[0]);
    Node* prev = head;

    for (int i=1; i<arr.size(); i++) {
        Node* temp = new Node(arr[i], prev, nullptr);
        prev->next = temp;
        prev = temp;
    }

    return head;
}

// O(1), O(1)
Node* deleteHeadInDLL (Node* head) {
    if (head == nullptr) {
        return nullptr;
    }
    if (head->next == nullptr) {
        delete head;
        return nullptr;
    }

    Node* pre = head->next;
    delete head;

    pre->prev = nullptr;

    return pre;
}

// O(n), O(1)
Node* deleteTailInDLL (Node* head) {
    if (head == nullptr) {
        return nullptr;
    }

    if (head->next == nullptr) {
        delete head;
        return nullptr;
    }

    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }

    temp->prev->next = nullptr;
    delete temp;

    return head;
}

// O(n), O(1)
Node* deleteKthNodeInDLL (Node* head, int k) {
    if (head == nullptr) {
        return head;
    }

    Node* temp = head;
    int count = 0;
    while (count != k && temp!=nullptr) {
        temp = temp->next;
        count++;
    }

    if (temp == nullptr) {
        return head;
    }

    if (temp->prev == nullptr) {
        Node* newHead = temp->next;
        if (newHead != nullptr) temp->next->prev = nullptr;
        delete temp;
        return newHead;
    }

    if (temp->next == nullptr) {
        temp->prev->next = nullptr;
        delete temp;
        return head;
    }

    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    delete temp;

    return head;
}

// O(1), O(1)
void deleteNodeInDLL (Node* node) {
    // given node is not head, delete given node in DLL
    Node* back = node->prev;
    Node* front = node->next;

    if (front == nullptr) {
        back->next = nullptr;
    }
    else {
        back->next = front;
        front->prev = back;
    }
    delete node;
}

// O(1), O(1)
Node* insertBeforeHeadDLL (Node* head, int x) {
    Node* temp = new Node(x, nullptr, head);
    
    if (head == nullptr) {
        return temp;
    }

    head->prev = temp;
    return temp;
}

// Stack - O(n), O(1)
Node* reverseDLL1 (Node* head) {
    stack <int> st;
    
    Node* temp = head;
    while (temp != nullptr) {
        st.push(temp->val);
        temp = temp->next;
    }

    temp = head;
    while (temp != nullptr) {
        temp->val = st.top();
        st.pop();
        temp = temp->next;
    }

    return head;
}

// Reverse arrows - O(n), O(1)
Node* reverseDLL2 (Node* head) {
    if (head == nullptr || head->next == nullptr) {
        return head;
    }
    
    Node* curr = head;
    Node* temp = nullptr;
    while (curr != nullptr) {
        temp = curr->prev;
        curr->prev = curr->next;
        curr->next = temp;

        curr = curr->prev;
    }

    return temp->prev;
}

int main() {
    Node* head = new Node(4);
    Node* middle = new Node(5);
    Node* end = new Node(6);
    head->next = middle;
    middle->prev = head;
    middle->next = end;
    end->prev = middle;
    head->prev = nullptr;
    end->next = nullptr;
    Node* lastEnd = new Node(8);
    end->next = lastEnd;
    lastEnd->next = nullptr;
    lastEnd->prev = end;

    // Node* head = arrayToDLL(vector <int> {1,2,3,4,5,6});
    // Node* newHead = deleteHeadInDLL(head);
    // Node* newHead = deleteTailInDLL(head);
    // Node* newHead = deleteKthNodeInDLL(head, 1);
    // deleteNodeInDLL(head->next);
    Node* newHead = reverseDLL2(head);

    printDLL(newHead);
    return 0;
}