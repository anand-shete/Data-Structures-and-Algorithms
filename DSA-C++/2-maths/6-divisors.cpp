#include <bits/stdc++.h>

using namespace std;

// brute force - O(n), O(n)
vector <int> divisors_1(int num) {
    vector <int> ans;

    for (int i=1; i<=num; ++i) {
        if (num % i == 0) {
            ans.push_back(i);
        }
    }

    return ans;
}

// optimal - O(sqrt(n)), O(n)
vector <int> divisors_2(int num) {
    vector <int> ans;

    for (int i=1; i*i<=num; ++i) {
        if (num % i == 0) {
            ans.push_back(i);

            if (i != num/i) {
                ans.push_back(num/i);
            }
        }
    }

    return ans;
}


int main() {
    int num = 36;

    for (int x:divisors_1(num)) cout << x << " ";
    
    // for (int x:divisors_2(num)) cout << x << " ";

    cout << endl;
    return 0;
}