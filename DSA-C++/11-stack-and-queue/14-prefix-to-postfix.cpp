#include <bits/stdc++.h>

using namespace std;

string prefix_to_postfix(string prefix) {
    stack <string> st;

    for (int i=prefix.size()-1; i>=0; --i) {
        char c = prefix[i];

        if (isalnum(c)) {
            st.push(string(1,c));
        }
        else {
            string op1 = st.top();
            st.pop();
            string op2 = st.top();
            st.pop();

            st.push(op1 + op2 + c);
        }
    }

    return st.top();
}

int main() {
    string prefix = "+A*B-^CDE";
    
    cout << prefix_to_postfix(prefix);

    cout << endl;
    return 0;
}