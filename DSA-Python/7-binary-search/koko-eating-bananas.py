# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Constraints:
# 1 <= piles.length <= 10⁴
# piles.length <= h <= 10⁹
# 1 <= piles[i] <= 10⁹



# brute - O(n), O(1)
def koko_eating_bananas_1(piles: list[int], h:int) -> int:
    totalHrs = 0
    
    for 
    


# binary search - O(n logn), O(1)
def can_eat_in_h(piles: list[int], h:int, k:int):
    hours = 0
    
    for x in piles:
        hours += k // x
        
    return hours <= h
    
    
    
def koko_eating_bananas_2(piles: list[int], h:int) -> int:
    low, high = 1, max(piles)
    res = 0
    
    while low < high:
        mid = (low + high) // 2
        
        if can_eat_in_h(piles, h, mid):
            low = mid + 1
            res = mid
        else:
            high = mid - 1
            
    return res




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        h = int(input())
        nums = list(map(int, input().split()))
        
        res = koko_eating_bananas_2(nums, h)
        
        print(res)