#include <bits/stdc++.h>

using namespace std;

int main() {
    // Stack data structure uses Last In, First Out principle

    // All operations take O(1)
    // Create a stack
    stack <int> st;

    // Push elements
    st.push(10);
    st.push(20);
    st.push(30);

    // Topmost element
    cout << "top element: " << st.top() << endl;

    // Remove last element
    st.pop();
    cout << "top element: " << st.top() << endl;

    // Size of stack
    cout << "size of stack: " << st.size() << endl;

    // Always check if stack is empty before pop or top
    cout << "is stack empty: " << st.empty() << endl;


    // traverse stack - O(n)
    while (!st.empty()) {
        cout << st.top() << endl;
        st.pop();
    }
    cout << endl;
    return 0;
}