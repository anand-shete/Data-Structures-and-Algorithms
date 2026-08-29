string = ["1", "2", "3", "4", "5"]

itr = map(int, string)

print(itr)
print(list(itr))




# 
def check_even(num:int) -> bool:
    return True if num % 2 == 0 else False

nums = [1,2,3,4,5,6]
print(list(map(check_even, nums)))
print(set(map(check_even, nums)))