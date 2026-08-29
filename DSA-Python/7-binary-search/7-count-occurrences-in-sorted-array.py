# You are given a sorted array containing N integers and a number X, you have to find the occurrences of X in the given array.



# brute force - O(n), O(1)


# binary search - O(log n), O(1)
def count_occurrences_in_sorted_array(nums: list[int], target: int) -> int:
    n = len(nums)
    low, high = 0, n-1
    first, last = -1, -1
    
    while low <= high:
        mid = (low + high) // 2
        
        if target <= nums[mid]:
            first = mid
            high = mid - 1
        else:
            low = mid + 1
            
    
    low, high = 0, n-1
    while low <= high:
        mid = (low + high) // 2
        
        if target < nums[mid]:
            high = mid - 1
        else:
            last = mid
            low = mid + 1
        
    if first == -1 or last == -1:
        return 0
    
    return last - first + 1




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        target = int(input())
        nums = list(map(int, input().split()))
        
        res = count_occurrences_in_sorted_array(nums, target)
        
        print(res)
        
        
'''
5
8
5 7 7 8 8 10
2
1 1 2 2 2 2 2 3
0

4
1 1 2 2 4 4 4 4 6 10
0
-2 -2 -1 0 1 2 3
'''