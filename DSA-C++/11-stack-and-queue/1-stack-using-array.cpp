#include <bits/stdc++.h>

using namespace std;

// O(1), O(n)
class ArrayStack {
vector <int> arr;
    
public:
    void push(int x) {
        arr.push_back(x);
    }

    int pop() {
        int top = arr.back();
        arr.pop_back();
        return top;
    }

    int top() {
        return arr.back();
    }

    bool isEmpty() {
        return arr.empty();
    }
};


int main() {
    ArrayStack st;
    st.push(1);
    st.push(2);
    st.push(3);
    st.push(4);

    while (st.isEmpty() != 1) {
        cout << st.top() << endl;
        st.pop();
    }

    cout << endl;
    return 0;
}