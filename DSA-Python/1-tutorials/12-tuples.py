# tuple is an immutable data structure which preseves insertion order


# create tuple - O(n)
tup1 = (40, 30, 20, 3.4)
tup2 = 10, 20, 30, 40, 50
tup3 = tuple()
tup4 = tuple([40, 50, 60])
tup5 = tuple('abcde')

print('empty tuple:',tup3)
print('tuple from list:',tup4)
print('tuple from string:',tup5)
print()


# check if element exists - O(n)
print('3 exists in tup1:', 3 in tup1)
print()


# count occurrences - O(n)
print('count of 10 in tup2:', tup2.count(10))
print('return first index or ValueError:', tup2.index(10))
print()


# access element - O(1)
print('element at index 0:',tup1[0])
print()


# slice tuple - O(k)
print('create tuple from index 1 to 2:',tup1[1:3])
print()


# length of tuple - O(1)
print('length of tup1:',len(tup1))
print()


# concatenate tuples - O(n+m)
print('concatenate tuples:',tup1+tup2)
print()


# unpack elements - O(n)
x, y, *rest = tup1
print(x)
print(y)
print(rest)
print()


# convert tuple to list - O(n)
tup1 = (1, 2, 3)
my_list = list(tup1)
print('convert tuple to list',my_list)