

# Worst case time complexity - O(n²)
# Avg. case time complexity - O(n. logn)
# Best case time complexity - O(n. logn)
# Space complexity - O(1)
def partition(low:int, high:int, nums:list) -> None:
    left, right, pivot = low, high, nums[low]
    
    while left < right:
        while nums[left] <= pivot and left < high:
            left += 1
            
        while nums[right] > pivot:
            right -= 1
            
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
    
    nums[low], nums[right] = nums[right], nums[low]
    
    return right
    
    
def quick_sort(low:int, high:int, nums:list) -> None:
    if low >= high:
        return
    
    partition_index = partition(low, high, nums)
    
    quick_sort(low, partition_index -1, nums)
    quick_sort(partition_index+1, high, nums)


if __name__ == "__main__": 
    loops = int(input())
    
    for _ in range(loops):
        nums = list(map(int, input().split()))
        
        quick_sort(0, len(nums) - 1, nums)
        
        print(*nums)
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
8 8 8 8 8 8 0
0 -1 -4 -4 -4 -4 0
1 2 3 4 5
'''