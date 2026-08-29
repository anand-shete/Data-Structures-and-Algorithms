#include <bits/stdc++.h>

using namespace std;
// Q. We are given an array asteroids of integers representing asteroids in a row. The indices of the asteroid in the array represent their relative position in space.
// For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
// Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.


// stack - O(n), O(n)
vector <int> asteroid_collision(vector <int> asteroids) {
    int n = asteroids.size();
    vector <int> ans;
    stack <int> st;

    for (int x:asteroids) {
        if (x > 0) {
            st.push(x);
        }
        else {
            while (!st.empty() && st.top() > 0 && st.top() < -x) {
                st.pop();
            }

            if (st.empty() || st.top()<0) {
                st.push(x);
            }

            if (!st.empty() && st.top() == -x) {
                st.pop();
            }
        }
    }

    while (!st.empty()) {
        ans.push_back(st.top());
        st.pop();
    }

    reverse(ans.begin(), ans.end());

    return ans;
}

int main() {
    vector <int> asteroids = {5,10,-5};

    vector <int> ans = asteroid_collision(asteroids);

    for (int x:ans) cout << x << " ";
    cout << endl;
    return 0;
}