#include <bits/stdc++.h>

using namespace std;

string postfix_to_prefix(string postfix) {
    stack <string> st;

    for (int i=0; i<postfix.size(); ++i) {
        char c = postfix[i];

        if (isalnum(c)) {
            st.push(string(1,c));
        }
        else {
            string op2 = st.top();
            st.pop();
            string op1 = st.top();
            st.pop();

            st.push(c + op1 + op2);
        }
    }

    return st.top();y
}

int main() {
    string postfix = "ABCD^E-*+";

    cout << postfix_to_prefix(postfix);

    cout << endl;
    return 0;
}