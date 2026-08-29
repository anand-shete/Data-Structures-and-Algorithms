#include <bits/stdc++.h>

using namespace std;

// Q. Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.


// brute force - O(n²), O(1)
int largest_rectangle_in_histogram_1(vector <int> heights) {
    int n = heights.size();
    int area = 0;

    for (int i=0; i<n; ++i) {
        int height = INT_MAX;

        for (int j=i; j<n; ++j) {
            height = min(height, heights[j]);

            area = max(area, (j-i+1) * height);
        }
    }

    return area;
}

// stack - O(n), O(n)
int largest_rectangle_in_histogram_2(vector <int> heights) {
    int n = heights.size();
    vector <int> prev_less(n, -1), next_less(n, n);
    stack <int> st;
    int max_area = 0;

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

        max_area = max(max_area, width * height);
    }

    return max_area;
}

int main() {
    vector <int> heights = {2,1,5,6,2,3};
    // heights = {2,1,5,6,7,2,2,3};

    // cout << largest_rectangle_in_histogram_1(heights) << endl;

    cout << largest_rectangle_in_histogram_2(heights) << endl;

    return 0;
}