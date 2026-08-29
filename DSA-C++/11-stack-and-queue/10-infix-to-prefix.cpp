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
    stack <int> st;
    string postfix = "";

    for (char c:infix) {
        if (isalnum(c)) {
            postfix += c;
        }
        else if (c == '(') {
            st.push(c);
        }
        else if (c == ')') {
            while (!st.empty() && st.top()!='(') {
                postfix += st.top();
                st.pop();
            }
            st.pop();
        }
        else {
            if (c == '^') {
                while (!st.empty() && prec(c)<=prec(st.top())) {
                    postfix += st.top();
                    st.pop();
                }
            }
            else {
                while (!st.empty() && prec(c) < prec(st.top())) {
                    postfix += st.top();
                    st.pop();
                }
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

string infix_to_prefix(string infix) {
    for (char &c:infix) {
        if (c == '(') {
            c = ')';
        }
        else if (c == ')') {
            c = '(';
        }
    }

    reverse(infix.begin(), infix.end());

    string postfix = infix_to_postfix(infix);
    reverse(postfix.begin(), postfix.end());

    return postfix;
}

int main() {
    string infix = "A+B*(C^D-E)";

    cout << infix_to_prefix(infix);

    cout << endl;
    return 0;
}