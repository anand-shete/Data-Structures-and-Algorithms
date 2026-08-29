# The lower bound algorithm finds the first or the smallest index in a sorted array where the value at that index is greater than or equal to a given key i.e. x.
# The lower bound is the smallest index, ind, where arr[ind] >= x. But if any such index is not found, the lower bound algorithm returns n i.e. size of the given array.




# closed interval template [low, high]
def lower_bound_1(nums: list[int], x:int) -> int:
    low, high = 0, len(nums) - 1
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if x <= nums[mid]:
            ans = nums[mid]
            high = mid -1
        else:
            low = mid + 1
            
    return ans




# halfopen interval template [low, high)
def lower_bound_2(nums: list[int], x:int) -> int:
    low, high = 0, len(nums)
    
    while low < high:
        mid = (low + high) // 2
        
        if x <= nums[mid]:
            high = mid
        else:
            low = mid + 1
    
    return nums[low]



if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        x = int(input())
        nums = list(map(int, input().split()))
        
        # res = lower_bound_1(nums, x)
        res = lower_bound_2(nums, x)
        
        print(res)
        
        
'''
5
9
-1 0 3 5 9 12
2
-1 0 3 5 9 12
4
-1 3 4 6 10 11
2
1 2 2 3
3
3
'''