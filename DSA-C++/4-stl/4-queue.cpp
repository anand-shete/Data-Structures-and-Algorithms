#include <bits/stdc++.h>

using namespace std;

int main() {
    // Queue data structure uses First In, First Out principle
    // All operations take O(1)
    queue <string> q;

    // Insert element at back
    q.push("lorem");
    q.push("ipsum");
    q.push("dor");
    q.push("amet");

    // First element
    cout << "first element of queue: " << q.front() << endl;

    // Last element
    cout << "last element of queue: " << q.back() << endl;

    // Remove first element
    q.pop();

    // Size of queue
    cout << "size of queue: " << q.size() << endl;

    // Check if empty
    cout << "is queue empty: " << q.empty() << endl;


    // traverse queue - O(n)
    while (!q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
    cout << endl << endl << endl;


    

    // Doubly ended queue allows you to insert and delete elements from both ends
    // Almost all operations take O(1)
    deque <int> dq;

    // insert to end of deque
    dq.push_back(1);
    dq.push_back(2);
    dq.push_back(3);
    dq.push_back(4);
    dq.push_back(5);

    // insert at front
    dq.push_front(0);

    // pop last element of deque (void function)
    dq.pop_back();

    // pop front element
    dq.pop_front();

    // front element
    cout << "front of deque: " <<  dq.front() << endl;
    
    // back element
    cout << "back of deque: " << dq.back() << endl;
    
    // access ith index element
    cout << "element at index 2: " << dq[2] << endl;

    // size of deque
    cout << "size of deque: " << dq.size() << endl;

    // check if deque empty
    cout << "is deque empty: " << dq.empty() << endl;


    // Traverse a deque - O(n)
    for (int x:dq) {
        cout << x << " ";
    } 
    cout << endl;

    // remove all elements - O(n)
    dq.clear();

    cout << endl << endl;




    // Priority Queue uses priority, where highest priority element is first
    // By default, priority queue is max heap

    priority_queue <string> max_pq;
    
    // Push elements - O(log n)
    max_pq.push("Abc");
    max_pq.push("xyz");
    max_pq.push("123");

    // Largest element - O(1)
    cout << "largest element: " << max_pq.top() << endl;

    // Pop element - O(log n)
    max_pq.pop();
    cout << "new largest element: " << max_pq.top() << endl;

    // size - O(1)
    cout << "size of priority queue: " << max_pq.size() << endl;

    // check if empty O(1)
    cout << "is priority queue empty: " << max_pq.empty() << endl;




    return 0;
}