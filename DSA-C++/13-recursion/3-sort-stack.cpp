#include <bits/stdc++.h>

using namespace std;

void insert(stack <int> &st, int temp) {
    if (st.empty() == 1 || temp >= st.top()) {
        st.push(temp);
        return;
    }

    int val = st.top();
    st.pop();
    insert(st, val);

    st.push(temp);
}

void sort_stack(stack <int> &st) {
    if (st.empty() != 1) {
        int temp = st.top();

        st.pop();

        sort_stack(st);

        insert(st, temp);
    }
}

int main() {
    stack <int> st;
    st.push(4);
    st.push(1);
    st.push(3);
    st.push(2);

    sort_stack(st);

    while (st.empty() != 1) {
        cout << st.top() << endl;
        st.pop();
    }
    return 0;
}