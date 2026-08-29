#include <bits/stdc++.h>

using namespace std;

string prefix_to_infix(string prefix) {
    stack <string> st;

    for (int i=prefix.size()-1; i>=0; --i) {
        char c = prefix[i];

        if (isalnum(c)) {
            st.push(string(1, c));
        }
        else {
            string op2 = st.top();
            st.pop();
            string op1 = st.top();
            st.pop();

            st.push("(" + op2 + c + op1 + ")");
        }
    }

    return st.top();
}

int main() {
    string prefix = "+A*B-^CDE";

    cout << prefix_to_infix(prefix);

    cout << endl;
    return 0;
}