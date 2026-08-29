#include <bits/stdc++.h>

using namespace std;

// Bitmasking - O(n²), O(1)
vector <string> all_subsequences_1(string &s) {
    vector <string> subseq;
    int n = s.size();
    int total = 1 << n;

    // there will be 2^n - 1 possible subsequences
    for (int mask=0; mask<total; ++mask) {
        string str = "";

        for (int i=0; i<n; ++i) {
            int test = 1 << i;
            if (mask & test) {
                str += s[i];
            }
        }
        subseq.push_back(str);
    }

    return subseq;
}


// Recursive call - O(n. 2^n), O(n)
void helper(const string &s, int idx, string &curr, vector <string> &ans) {
    if (idx == s.size()) {
        ans.push_back(curr);
        return;
    }

    curr.push_back(s[idx]);
    helper(s, idx+1, curr, ans);

    curr.pop_back();
    helper(s, idx+1, curr, ans);
}

vector <string> all_subsequences_2(string &s) {
    vector <string> ans;
    string curr = "";

    helper(s, 0, curr, ans);
    return ans;
}

int main() {
    string s = "abc";
    
    // for (string str:all_subsequences_1(s)) cout << str << " ";
    for (string str:all_subsequences_2(s)) cout << str << " ";

    cout << endl;
    return 0;
}