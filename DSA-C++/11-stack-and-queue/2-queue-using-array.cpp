#include <bits/stdc++.h>

using namespace std;


// O(1), O(n)
class ArrayQueue {
vector <int> arr;
int frontIdx = 0;

public:
    void push(int x) {
        arr.push_back(x);
    }

    int pop() {
        if (isEmpty()) return -1;
        int front = arr[frontIdx];
        frontIdx++;
        return front;
    }

    int peek() {
        if (isEmpty()) return -1;
        return arr[frontIdx];
    }

    bool isEmpty() {
        return frontIdx >= arr.size();
    }
};

int main() {
    ArrayQueue q;
    q.push(1);
    q.push(2);
    q.push(3);
    q.push(4);

    while (q.isEmpty() != 1) {
        cout << q.peek() << " ";
        q.pop();
    }

    cout << endl;
    return 0;
}