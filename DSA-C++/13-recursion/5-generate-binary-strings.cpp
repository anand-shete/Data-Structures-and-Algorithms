#include <bits/stdc++.h>

using namespace std;

// O(2^n), O(n)
void generate_binary_strings(int n, string curr, vector <string> &ans) {
    if (curr.size() == n) {
        ans.push_back(curr);
        return;
    }

    generate_binary_strings(n, curr+"0", ans);

    if (curr.empty() || curr.back()!='1') {
        generate_binary_strings(n, curr+"1", ans);
    }

}

int main() {
    int n = 3;
    string curr = "";
    vector <string> ans;

    generate_binary_strings(n, curr, ans);

    for (string str:ans) {
        cout << str << " ";
    }
    cout << endl;
    return 0;
}