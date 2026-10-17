"""
`map` function applies operation to each element and returns iterator - O(n), O(1)
returns iterator object which are single use iterables
"""

def transform(x:str) -> int:
    return int(x)

l = ["1","2","2","2","2","3","4","4"]
itr = map(transform, l)
l = list(itr)
print("iterators are single use:",itr)
print("iterator to list:",l)
print("wrong iterator to list:",set(itr))
print("correct iterator to set:",set(l))
print()



"""
`filter` constructs iterator from elements that return `True` - O(n), O(1)
returns iterator object
"""
def check_even(x:int) -> bool:
    return True if x % 2 == 0 else False

l = [1,2,3,4,5,6]
itr = filter(check_even, l)
print("filter even numbers:",list(itr))
print()



"""
`reduce(function, iterable, initial)` accumulates integer to single value
"""
from functools import reduce
l = [1,2,3,4]
sum_reduce = reduce(lambda x,y: x+y, l, 1)
print("reduce:",sum_reduce)