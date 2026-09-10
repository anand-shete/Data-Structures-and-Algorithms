# You are given an integer array bloomDay, an integer m and an integer k.
# You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
# The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
# Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


# Constraints:
# bloomDay.length == n
# 1 <= n <= 105
# 1 <= bloomDay[i] <= 109
# 1 <= m <= 106
# 1 <= k <= n
# first input line is bloomDay list
# second input is integer m
# third input line represents integer k




# brute force - O(n⁢⁣.max(bloomDay)), O(1)
def minimum_number_of_days_to_make_bouquets_1(bloomDay:list[int], m:int, k:int):
    min_days = 0
    
    for i in range(min(bloomDay), max(bloomDay)+1):
        if can_make_bouquets(bloomDay, m, i, k):
            return i
                
    return -1




# binary search - O(N.log(max(bloomDay) - min(bloomDay))), O(1)
def minimum_number_of_days_to_make_bouquets_2(bloomDay: list[int], m:int, k:int):
    if m * k > len(bloomDay):
        return -1
    
    low, high = min(bloomDay), max(bloomDay)
    
    while low < high:
        mid = (low + high) // 2
        
        if can_make_bouquets(bloomDay, m, mid, k):
            high = mid
        else:
            low = mid + 1
            
    return low


def can_make_bouquets(bloomDay: list[int], m:int, mid:int, k:int):
    adj, bouq = 0, 0
    
    for bloom in bloomDay:
        if bloom <= mid:
            adj += 1
            
            if adj == k:
                bouq += 1
                adj = 0
                
        else:
            adj = 0
            
    return bouq >= m
        
        
    
if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        bloomDay = list(map(int, input().split()))
        m = int(input())
        k = int(input())
        
        # result = minimum_number_of_days_to_make_bouquets_1(bloomDay, m, k)
        result = minimum_number_of_days_to_make_bouquets_2(bloomDay, m, k)
        
        print(result)