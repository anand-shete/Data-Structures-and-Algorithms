# There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array 'cardPoints'.
# In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.
# Your score is the sum of the points of the cards you have taken.
# Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

# Constraints:
# 1 <= cardPoints.length <= 10⁵
# 1 <= cardPoints[i] <= 10⁴
# 1 <= k <= cardPoints.length



# brute force - O(n²), O(1)
def max_card_points_1(cardPoints: list[int], k:int) -> int:
    n = len(cardPoints)
    max_points = 0
    
    for i in range(k+1):
        temp = 0
        
        for j in range(i):
            temp += cardPoints[j]
        
        for j in range(k-i):
            temp += cardPoints[n-1-j]
            
        max_points = max(max_points, temp)
        
    return max_points




# sliding window - O(n), O(1)
def max_card_points_2(cardPoints: list[int], k:int) -> int:
    n = len(cardPoints)
    window = sum(cardPoints[:k])
    max_points = window
    
    for i in range(k):
        window -= cardPoints[k-1-i]
        window += cardPoints[n-1-i]
        
        max_points = max(max_points, window)
        
    return max_points
    
    


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        k = int(input())
        nums = list(map(int, input().split()))
        
        res = max_card_points_1(nums, k)
        res = max_card_points_2(nums, k)
        
        print(res)
        
        
'''
5
3
1 2 3 4 5 6 1
2
2 2 2
7
9 7 7 9 7 7 9
3
4 5 3 1 2 1 2
4
1 2 1 2 4 5 3
'''