#include <bits/stdc++.h>

using namespace std;
// Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

// Implement the FreqStack class:

// - FreqStack() constructs an empty frequency stack.
// - void push(int val) pushes an integer val onto the top of the stack.
// - int pop() removes and returns the most frequent element in the stack.
//   If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.


// O(1), O(n)
struct FreqStack {
    int maxFreq;
    unordered_map <int, int> freqMap;
    unordered_map <int, vector <int>> groupFreqMap;

    FreqStack() {
        maxFreq = 0;
    };

    void push(int val) {
        freqMap[val]++;
        int freq = freqMap[val];

        if (freq > maxFreq) {
            maxFreq = freq;
        }

        groupFreqMap[freq].push_back(val);
    }

    int pop() {
        int ele = groupFreqMap[maxFreq].back();

        groupFreqMap[maxFreq].pop_back();

        freqMap[ele]--;

        if (groupFreqMap[maxFreq].empty()) {
            maxFreq--;
        }

        return ele;
    }
};


int main() {
    FreqStack freqSt;

    freqSt.push(5);     // [5]
    freqSt.push(7);     // [5,7]
    freqSt.push(5);     // [5,7,5]
    freqSt.push(7);     // [5,7,5,7]
    freqSt.push(4);     // [5,7,5,7,4]
    freqSt.push(5);     // [5,7,5,7,4,5]
    cout << freqSt.pop() << endl;       // return 5, as 5 is most frequent [5,7,5,7,4]
    cout << freqSt.pop() << endl;       // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top [5,7,5,4]
    cout << freqSt.pop() << endl;       // return 5, as 5 is the most frequent [5,7,4]
    cout << freqSt.pop() << endl;       // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top [5,7]

    return 0;
}