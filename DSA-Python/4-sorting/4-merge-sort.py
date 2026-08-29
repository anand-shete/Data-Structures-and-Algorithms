

# Worst case time complexity - O(n . log(n))
# Avg. case time complexity - O(n . log(n))
# Best case time complexity - O(n . log(n))
# Space complexity - O(n)
def merge(low:int, mid:int, high:int, nums:list) -> None:
    left, right = low, mid+1
    temp = []
    
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
            
    while right <= high:
        temp.append(nums[right])
        right += 1
        
    while left <= mid:
        temp.append(nums[left])
        left += 1
        
    for i in range(low, high+1):
        nums[i] = temp[i-low]
         

def divide(low: int, high:int, nums:list) -> None:
    if low >= high:
        return
    
    mid = (low + high) // 2
    
    divide(low, mid, nums)
    divide(mid+1, high, nums)
    
    merge(low, mid, high, nums)
    
    
if __name__ == "__main__":
    loops = int(input())
    
    for _ in range(loops):
        nums = list(map(int, input().split()))

        divide(0, len(nums)-1, nums)
        
        print(*nums)
        
        
        
'''
5
3 12 2 6 24 43
-2 45 54 3 12 23
8 8 8 8 8 8 0
0 -1 -4 -4 -4 -4 0
1, 2, 3, 4, 5
'''