# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


# brute force - O(n), O(1)


# binary search - O(log n), O(1)
def search_insert_position(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    ans = len(nums)
    
    while low <= high:
        mid = (low + high) // 2
        
        if target <= nums[mid]:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return ans




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = search_insert_position(nums, target)
        
        print(res)
        
        
        
'''
3
5
1 3 5 6
2
1 3 5 6
7
1 3 5 6
'''