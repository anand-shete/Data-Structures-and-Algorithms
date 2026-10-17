# set is an unordered collection of immutable and unique elements


uset = {1, 2, 2, 2, 3, 3, 4, 6, 8, 9}
empty_set = set()


# check if element exists - O(1)
print('check 8 exists:', 8 in uset)
print()


# add element - O(1)
print('insert 5 to set:',uset.add(5))
print()


# remove element - O(1)
print('remove 3 from set:', uset.discard(3))
print('raise KeyError if 4 not found:', uset.remove(4))
print(uset)
print()


# pop random element - O(1)
print('pop random element:', uset.pop())


# length of set - O(1)
print('length of set:',len(uset))


# clear set - O(1)
print('clear all elements:',uset.clear())
print('\n')



# convert list to set - O(n)
nums = [23, 45, 56, 78]
set2 = set(nums)
print('convert list to set:',set2)
print()


# union of sets - O(n1 + n2)
uset = {1,2,3,4}
set2 = {3,4,5,6}
print('unique elements from both set:',uset.union(set2))


# common elements - O(min(n1, n2))
print('common elements of both set:',uset.intersection(set2))


# difference between set - O(n1)
print('remove elemnts of uset in set2:',set2 - uset)


# symmetric difference - O(n1 + n2)
print('remove overlapping elements:', uset ^ set2)
print('\n')



# iterate set - O(n)
for x in uset:
    print(x, end=' ')