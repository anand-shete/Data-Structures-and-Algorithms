# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.

# Constraints:
# 1 <= piles.length <= 10⁴
# piles.length <= h <= 10⁹
# 1 <= piles[i] <= 10⁹
from math import ceil


# brute - O(n.max(piles)), O(1)
def koko_eating_bananas_1(piles: list[int], h:int) -> int:
    k = 1
    
    while not can_eat_in_h(piles, k, h):
        k += 1 
    
    return k




# binary search - O(n log(max(piles))), O(1)
def koko_eating_bananas_2(piles: list[int], h:int) -> int:
    low, high = 1, max(piles)
    
    while low < high:
        mid = (low + high) // 2
        
        # higher speed means less hours taken to eat all bananas
        # if koko can eat at mid hrs, she can eat at mid+1, mid+2, ...
        if can_eat_in_h(piles, mid, h):
            result = mid
            
            # to find minimum, decrease high
            high = mid
        else:
            low = mid + 1
            
    return low


def can_eat_in_h(piles: list[int], mid:int, h:int):
    hrs_taken = 0
    
    for x in piles:
        hrs_taken += ceil(x / mid)
        
    return hrs_taken <= h




if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        h = int(input())
        nums = list(map(int, input().split()))
        
        res = koko_eating_bananas_1(nums, h)
        # res = koko_eating_bananas_2(nums, h)
        
        print(res)
        
        
        
'''
3
8
3 6 7 11
5
30 11 23 4 20
6
30 11 23 4 20
'''