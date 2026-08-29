#include <bits/stdc++.h>

using namespace std;
// Q. Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

// stack - O(n²), O(n)
int largest_histogram(vector <int> heights) {
    int n = heights.size();
    vector <int> prev_less(n,-1), next_less(n,n);
    int maxArea = 0;
    stack <int> st;

    for (int i=0; i<n; ++i) {
        while (!st.empty() && heights[st.top()] >= heights[i]) {
            st.pop();
        }

        if (!st.empty()) prev_less[i] = st.top();
        st.push(i);
    }

    while (!st.empty()) st.pop();

    for (int i=n-1; i>=0; --i) {
        while (!st.empty() && heights[st.top()] >= heights[i]) {
            st.pop();
        }

        if (!st.empty()) next_less[i] = st.top();
        st.push(i);
    }

    for (int i=0; i<n; ++i) {
        int width = next_less[i] - prev_less[i] - 1;
        int height = heights[i];

        maxArea = max(maxArea, width * height);
    }

    return maxArea;
}

int maximum_rectangle(vector <vector <char>> matrix) {
    int ans = 0, rows = matrix.size(), cols = matrix[0].size();
    vector <int> heights(cols, 0);

    for (int i=0; i<rows; ++i) {

        for (int j=i; j<cols; ++j) {
            if (matrix[i][j] == '1') {
                heights[j] += 1;
            }
            else {
                heights[j] = 0;
            }
        }

        ans = max(ans, largest_histogram(heights));
    }

    return ans;
}


int main() {
    vector <vector <char>> matrix = 
    { {'1','0','1','0','0'} , {'1','0','1','1','1'} , {'1','1','1','1','1'} , {'1','0','0','1','0'} };

    cout << maximum_rectangle(matrix) << endl;

    
    return 0;
}