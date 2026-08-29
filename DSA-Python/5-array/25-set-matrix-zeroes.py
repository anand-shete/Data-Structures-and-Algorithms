# Given an m x n integer matrix 'matrix', if an element is '0', set its entire row and column to 0's in place.



# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2³¹ <= matrix[i][j] <= 2³¹ - 1


# Brute force - O(m.n), O(m+n)
def set_matrix_zeroes_1(matrix:list[list[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    row_zero, col_zero = [],[]
    
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                row_zero.append(i)
                col_zero.append(j)
    
    for ith in row_zero:
        for jth in range(len(matrix[0])):
            matrix[ith][jth] = 0
            
    for jth in col_zero:
        for ith in range(len(matrix)):
            matrix[ith][jth] = 0
    


# Optimal - O(m.n), O(1)
def set_matrix_zeroes_2(matrix: list[list[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    first_row_zero, first_col_zero = False, False
    
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break
        
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break
    
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
                
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
                
    if first_row_zero:
        for i in range(cols):
            matrix[0][i] = 0
            
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0
    
    


if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        rows, cols = map(int,input().split())
        
        matrix = []
        
        for _ in range(rows):
            row = list(map(int, input().split()))
            matrix.append(row)
            
            
        # set_matrix_zeroes_1(matrix)
        
        set_matrix_zeroes_2(matrix)
        
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(matrix[i][j], end=' ')
            print()
        print()
        
        
'''
5
3 3
1 1 1
1 0 1
1 1 1
3 4
0 1 2 0
3 4 5 2
1 3 1 5
3 4 
1 0 3
4 5 6
7 8 9
3 3
1 2 3
0 5 6
7 8 9
3 3
0 2 3
4 5 6
7 8 9
'''