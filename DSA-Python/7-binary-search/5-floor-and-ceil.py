# Given an sorted array arr of n integers and an integer x. Find the floor and ceiling of x in arr[0..n-1]. 
# The floor of x is the largest element in the array which is smaller than or equal to x. 
# The ceiling of x is the smallest element in the array greater than or equal to x
# Return -1 if floor or ceil in array does not exists



# brute force - O(n), O(1)

# binary search - O(log n), O(1)
def get_floor(nums: list[int], x:int) -> int:
    low, high = 0, len(nums)-1
    floor = -1
    
    while low <= high:
        mid = (low + high) // 2

        if nums[mid] <= x:
            floor = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return -1 if floor == -1 else nums[floor]

        
def get_ceil(nums: list[int], x:int) -> int:
    low, high = 0, len(nums) - 1
    ceil = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] >= x:
            ceil = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return -1 if ceil == -1 else nums[ceil]




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        x = int(input())
        nums = list(map(int, input().split()))
        
        floor = get_floor(nums, x)
        ceil = get_ceil(nums, x)
        
        print(floor,ceil)
        
        
        
        
'''
4
5
1 3 5 6
2
1 3 5 6
7
1 3 5 6
0
1 3 5 6
'''