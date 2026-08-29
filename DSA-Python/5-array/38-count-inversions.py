# Given an array of N integers, count the inversion of the array (using merge-sort).
# Inversion of an array: for all i & j < size of array, if i < j then you have to find pair (A[i],A[j]) such that A[j] < A[i].




# brute force - O(n²), O(1)
def count_inversions_1(nums: list[int]) -> int:
    pairs, n = 0, len(nums)
    
    for i in range(n):
        
        for j in range(i+1, n):
            if nums[i] > nums[j]:
                pairs += 1
                
    return pairs



# merge sort and count inversion - O(n. logn), O(n)
def merge(nums: list[int], low:int, mid:int, high:int) -> int:
    left, right = low, mid+1
    cnt = 0
    temp = []
    
    while left <= mid and right <= high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            cnt += mid - left + 1
            right += 1
        
    while left <= mid:
        temp.append(nums[left])
        left += 1
    
    while right <= high:
        temp.append(nums[right])
        right += 1
        
    for i in range(low, high+1):
        nums[i] = temp[i-low]
    
    return cnt

    
def count_inversions_2(nums: list[int], low:int, high:int) -> int:
    cnt = 0
    
    if low >= high:
        return cnt
    
    mid = (low + high) // 2
    cnt += count_inversions_2(nums, low, mid)
    cnt += count_inversions_2(nums, mid+1, high)
    
    cnt += merge(nums, low, mid, high) 
    
    return cnt
    
    
if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = count_inversions_1(nums)
        res = count_inversions_2(nums, 0, len(nums)-1)
        
        print(res)
        
        
        
'''
3
1 2 3 4 5
5 4 3 2 1
5 3 2 1 4
'''