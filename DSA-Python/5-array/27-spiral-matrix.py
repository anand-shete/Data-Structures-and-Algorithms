# Given an m x n matrix, return all elements of the matrix in spiral order.
# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100



# Optimal - O(rows.cols), O(1)
def spiral_matrix_1(matrix:list[list[int]]) -> list[int]:
    rows, cols = len(matrix), len(matrix[0])
    top, right, bottom, left = 0, cols, rows, 0
    res = []
    
    while top < bottom and left < right:
        for i in range(left, right):
           res.append(matrix[top][i])
        top += 1
        
        for i in range(top, bottom):
            res.append(matrix[i][right-1])
        right -= 1
        
        if top < bottom:
            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1
        
        if left < right:
            for i in range(bottom-1, top-1, -1):
                res.append(matrix[i][left])
            left += 1
        
    return res
        
            


if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        rows, cols = map(int, input().split())
        
        matrix = []
        
        for _ in range(rows):
            row = list(map(int, input().split()))
            matrix.append(row)
            
            
        res = spiral_matrix_1(matrix)
        
        # spiral_matrix_2(matrix)
        
        
        print(res, end='\n\n')
        
        
'''
5
3 3
1 2 3 
4 5 6
7 8 9
3 4
1 2 3 4
5 6 7 8
9 10 11 12
3 4 
1 0 3 -3
4 5 6 -2
7 8 9 -1
3 1
1
2
3
1 3
1 2 3
'''