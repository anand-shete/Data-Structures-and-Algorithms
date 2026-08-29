#include <bits/stdc++.h>

using namespace std;

// O(n²), O(n)
void insert_bottom(stack <int> &st, int temp) {
    if (st.empty() == 1) {
        st.push(temp);
        return;
    }

    int val = st.top();
    st.pop();

    insert_bottom(st, temp);
    st.push(val);
}

void reverse_stack(stack <int> &st) {
    if (st.empty() == 1) {
        return;
    }

    int temp = st.top();
    st.pop();

    reverse_stack(st);

    insert_bottom(st, temp);
}

int main() {
    stack <int> st;
    st.push(2);
    st.push(3);
    st.push(1);
    st.push(4);

    reverse_stack(st);

    while (st.empty() != 1) {
        cout << st.top() << endl;
        st.pop();
    }
    return 0;
}