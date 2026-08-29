# List is mutable dynamic array that handles resizing automatically under the hood


# create list
# list can contain elements of different data types
list1 = [3, 5, 7 , 9, 10 ]
init_0 = [0] * 10
copied = list1[:]
long = list(range(10))

print('python list is c++ vector: ', list1)
print('init list with all zeros:', init_0)
print('copied initialzation:', copied)
print('ranged list:', long)
print()


# access element - O(1)
print('element at idx 3:', list1[3])
print('element at idx -3:', list1[-3])
print()


# update element - O(1)
list1[3] = 14
print('update element at idx 3:', list1)
print()


# insert at idx - O(n)
list1.insert(3, 31)
print('insert at idx 3:',list1)
print()


# insert at end - O(1) amortised
list1.append(40)
print('insert single at end:', list1)


# extend list - O(k) where k is items added to list
list1.extend([3,4])
print('insert multiple at end:',list1)
print()


# remove and return last element - O(1)
print('pop last element:', list1.pop())


# remove element from list - O(n)
l = list1.pop(3)
print("remove element at idx 3: ", list1)
print()


# length of list - O(1)
print('length of list:', len(list1))
print()


# is list empty - O(1)
print('list is empty:', len(list1)==0)
if not list:
    print('list is empty')
print()


# count occurrences - O(n)
print('number of occurrences of 3:', list1.count(3))
print()


# remove all elements - O(n)
list1.clear()
print("remove all elements:", list1)
print()


# sort list in-place - O(n.logn), O(n) uses Timsort
list2 = [45, 64, 3, 2, 7, 9]
print('sort function:',list2.sort())


# sort and return list - O(n.logn)
print('sorted fuction: ',sorted(list2))


# sort in decreasing order - O(n.logn)
list2.sort(reverse=True)
print("decreasing sort:",list2)
print()


# reverse function - O(n), O(1)
list2 = [2, 3, 7, 9, 45, 64]
print('reverse function:',list2.reverse())


# slice list - O(k) where k is no. of elements sliced
list2 = [2, 3, 7, 9, 45, 64]
print("slice from idx 0 to 3:",list2[:4])
print('slice reverse:',list2[::-1])
print()


# check if element exists - O(n)
list2 = [10, 20, 30]
print("20 exists in list:", 20 in list2)
print()


# check if list empty - O(1)
print('is list2 empty:', not list2)
print('\n')



# list comprehensions allow us to create list quickly
squares = [x * x for x in range(1,6)]
print('list comprehension:',squares)
evens = [x * 2 for x in range(0,5)]
print('first 5 even numbers:',evens)
print()


# join - O(n) where n is final length of string
list2 = ["Rohan", "Mohan", "Soham"]
print('only str can use join:', "::".join(list2))
print()


# slice nums on right side means create a copy - O(n), O(n)
nums = [1,2,3,4,5]
copy = nums[:]
print('copy of nums:', copy)


# slice nums on left side modifies original list - O(n+k) where n original elements remove and k elements copied from list, O(1)
nums[:] = list2
print('orignal nums:', nums)
print('\n')



# iterate list with element - O(n)
# x is temporary variable which does not affect array
list2 = [10, 20, 30]
for x in list2:
    print(x, end=' ')
print('\n')


# iterate list using for loop - O(n)
for i in range(len(list2)):
    print(list2[i], end=' ')
print('\n')


# pass optional start argument in enumerate - O(n)
for idx, ele in enumerate(list2, start=1):
    print(f'{idx}=>{ele}')
print('\n')