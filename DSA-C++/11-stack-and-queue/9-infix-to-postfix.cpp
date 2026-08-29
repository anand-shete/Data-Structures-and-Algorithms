#include <bits/stdc++.h>

using namespace std;

int prec(char c) {
    if (c == '^') return 3;
    else if (c == '/' || c == '*') return 2;
    else if (c == '-' || c == '+') return 1;
    else return 0;
}

// O(n), O(n)
string infix_to_postfix(string infix) {
    stack <char> st; 
    string postfix = "";

    for (char c:infix) {
        if (isalnum(c)) {
            postfix += c;
        }
        else if (c == '(') {
            st.push(c);
        }
        else if (c == ')') {
            while (!st.empty() && st.top() != '(') {
                postfix += st.top();
                st.pop();
            }
            st.pop();
        }
        else {
            while (!st.empty() && prec(st.top()) >= prec(c)) {
                postfix += st.top();
                st.pop();
            }
            st.push(c);
        }
    }

    while (!st.empty()) {
        postfix += st.top();
        st.pop();
    }

    return postfix;
}

int main() {
    string infix = "A+B*(C^D-E)";

    cout << infix_to_postfix(infix);

    cout << endl;
    return 0;
}