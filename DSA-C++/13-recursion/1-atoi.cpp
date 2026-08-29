#include <bits/stdc++.h>

using namespace std;

// O(N), O(N)
int recursive_call(const string &s, long long ans, int i, int sign) {
    if (i>=s.size() || isdigit(s[i])==0) {
        return (int)sign * ans;
    }

    ans = ans*10 + s[i]-'0';
    if (sign*ans <= INT_MIN) return INT_MIN;
    if (sign*ans >= INT_MAX) return INT_MAX;

    return recursive_call(s, ans, i+1, sign);
}

int my_atoi(string s, int i=0) {
    while (i<s.size() && s[i] == ' ') {
        i++;
    }

    if (i == s.size()) return 0;
    
    int sign = 1;
    if (s[i]=='+' || s[i] == '-') {
        if (s[i] == '-') sign = -1;
        i++;
    }

    return recursive_call(s, 0, i, sign);
}

int main() {
    string myAtoi = "     -";
    
    cout << my_atoi(myAtoi);

    cout << endl;
    return 0;
}