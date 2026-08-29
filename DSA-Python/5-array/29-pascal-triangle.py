# Given an integer 'numRows', return the first numRows of Pascal's triangle. In Pascal's triangle, each number is the sum of the two numbers directly above it

# Constraints:
# 1 <= numRows <= 30


# brute force - O(n²), O(1)
def pascal_triangle_1(numRows:int) -> list[list[int]]:
    res = []
    
    for i in range(1,numRows+1):
        temp = []
            
        for j in range(1,i+1):
            if j==1 or j==i:
                temp.append(1)
            else:
                temp.append(res[i-2][j-2] + res[i-2][j-1])
            
        res.append(temp)
        
    return res
        
        
if __name__ == "__main__": 
    loop = int(input())

    for _ in range(loop):
        numRows = int(input())
        
        res = pascal_triangle_1(numRows)
        
        print(res, end='\n\n')
        
        
'''
5
5
4
6
9
10
'''