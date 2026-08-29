#include <bits/stdc++.h>

using namespace std;

// O(n), O(n)
class QueueStack {
queue <int> q;

public:
    void push(int x) {
        int n = q.size();
        
        q.push(x);
        for (int i=0; i<n; ++i) {
            q.push(q.front());
            q.pop();
        }
    }
    int pop() {
        if (empty()) return -1;
        int top = q.front();
        q.pop();
        return top;
    }
    int top() {
        if (empty()) return -1;
        return q.front();
    }
    bool empty() {
        return q.empty();
    }
};

int main() {
    QueueStack st;

    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    while (st.empty() != 1) {
        cout << st.top() << endl;
        st.pop();
    }
    
    cout << endl;
    return 0;
}