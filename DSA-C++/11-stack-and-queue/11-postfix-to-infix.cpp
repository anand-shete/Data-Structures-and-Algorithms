#include <bits/stdc++.h>

using namespace std;

string postfix_to_infix(string postfix) {
    stack <string> st;
    string infix = "";

    for (char c:postfix) {
        if (isalnum(c)) {
            st.push(string(1,c));
        }
        else {
            string operand1 = st.top();
            st.pop();
            string operand2 = st.top();
            st.pop();

            // op1 is actually op2
            st.push("(" + operand2 + c + operand1 + ")");
        }
    }

    return st.top();
}

int main() {
    string postfix = "ABCD^E-*+";

    cout << postfix_to_infix(postfix);

    cout << endl;
    return 0;
}