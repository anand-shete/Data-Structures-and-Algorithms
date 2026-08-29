#include <bits/stdc++.h>

using namespace std;

// O(n), O(n)
class StackQueue {
stack <int> st1, st2;

public:
    StackQueue() {}

    void push(int x) {
        size_t n = st1.size();
        for (size_t i=0; i<n; ++i) {
            st2.push(st1.top());
            st1.pop();
        }

        st1.push(x);
        for (size_t i=0; i<n; ++i) {
            st1.push(st2.top());
            st2.pop();
        }        
    }

    int pop() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        int front = st1.top();
        st1.pop();

        return front;
    }
    
    int peek() {
        if (empty()) {
            throw runtime_error("Stack is empty");
        }
        return st1.top();
    }

    bool empty() {
        return st1.empty();
    }
};

int main() {
    StackQueue q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);

    while (q.empty() != 1) {
        cout << q.pop() << " ";
    }

    cout << endl;
    return 0;
}