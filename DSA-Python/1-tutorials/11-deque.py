# queue follows first in first out principle
# python standard implementation of queue is doubly ended queue
from collections import deque


# create queue - O(1)
q = deque()


# add element to back - O(1)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
print()


# remove front element or raise IndexError - O(1)
print('pop front:',q.popleft())
print()


# peek front element or raise IndexError - O(1)
print('peek front:',q[0])
print()


# check size of queue - O(1)
print('length of queue:',len(q))
print()


# remove all elements - O(1)
# q.clear()


# check if queue empty - O(1)
print('is queue empty:', not q)
print('\n')


# iterate queue - O(n)
for x in q:
    print(x, end=' ')