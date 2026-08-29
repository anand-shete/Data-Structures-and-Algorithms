# Given an integer array nums, return the number of reverse pairs in the array.
# A reverse pair is a pair (i, j) where:
# 0 <= i < j < nums.length and
# nums[i] > 2 * nums[j].

# Constraints:
# 1 <= nums.length <= 5 * 10⁴
# -2³¹ <= nums[i] <= 2³¹ - 1



# brute force - O(n²), O(1)
def reverse_pairs_1(nums:list[int]) -> int:
    pairs, n = 0, len(nums)
    
    for i in range(n):
        
        for j in range(i+1, n):
            if nums[i] > 2 * nums[j]:
                pairs += 1

    return pairs



# custom merge sort - O(n. logn), O(1)
def merge(nums:list[int], low:int, mid:int, high:int) -> None:
    left, right = low, mid+1
    temp = []
    
    while left<=mid and right<=high:
        if nums[left] <= nums[right]:
            temp.append(nums[left])
            left += 1
        else:
            temp.append(nums[right])
            right += 1
            
    while left <= mid:
        temp.append(nums[left])
        left += 1
        
    while right <= high:
        temp.append(nums[right])
        right += 1
        
    for i in range(low, high+1):
        nums[i] = temp[i-low]
        

def count_inversions(nums: list[int], low:int, mid:int, high:int) -> int:
    left, right = low, mid+1
    cnt = 0
    
    for i in range(low, mid+1):
        while right <= high and nums[i] > 2 * nums[right]:
            right += 1
        cnt += right - (mid + 1)
        
    return cnt

    
def reverse_pairs_2(nums: list[int], low:int, high:int) -> int:
    cnt = 0
    if low >= high:
        return cnt
    
    mid = (low + high) // 2
    cnt += reverse_pairs_2(nums, low, mid)
    cnt += reverse_pairs_2(nums, mid + 1, high)
    
    cnt += count_inversions(nums, low, mid, high)
    
    merge(nums, low, mid, high)
    
    return cnt
    
    
    

if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        nums = list(map(int, input().split()))
        
        # res = reverse_pairs_1(nums)
        res = reverse_pairs_2(nums, 0, len(nums)-1)
        
        print(res)
        
        
'''
2
1 3 2 3 1
2 4 3 5 1
'''