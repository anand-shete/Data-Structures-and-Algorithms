# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input

# Constraints:
# 1 <= intervals.length <= 100
# intervals[i].length == 2
# 0 <= starti <= endi <= 100


# brute force - O(n²), O(1)
def merge_intervals_1(intervals:list[list[int]]) -> list[list[int]]:
    n = len(intervals)
    res = []
    
    intervals.sort()
    
    i = 0
    while i < n:
        j = i+1
        start, end = intervals[i][0], intervals[i][1]
        
        while j < n and end >= intervals[j][0]:
            end = max(end, intervals[j][1])
            j += 1
            
        res.append([start, end])
        
        i = j
        
    return res
            
            
           
# optimal - O(n.logn), O(1) 
def merge_intervals_2(intervals:list[list[int]]) -> list[list[int]]:
    n = len(intervals)
    res = []
    
    intervals.sort()
    
    for interval in intervals:
        if not res or res[-1][1] < interval[0]:
            res.append(interval)
        else:
            res[-1][1] = max(res[-1][1], interval[1])
            
    return res
    
    


if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        intervals = []
        ele = int(input())
        
        for _ in range(ele):
            intervals.append(list(map(int, input().split())))
            
        res = merge_intervals_1(intervals)
        res = merge_intervals_2(intervals)
        
        print(res, end='\n\n')
        
'''
5
4
1 3
8 10
2 6
15 18
2
1 4
4 5
2
4 7
1 4
4
1 10
2 3
4 5
6 7
5
4 7
1 4
5 6
7 9
11 15
'''