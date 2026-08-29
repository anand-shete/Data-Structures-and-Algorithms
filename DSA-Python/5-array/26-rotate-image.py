# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000



# brute force - O(n²), O(n²)
def rotate_image_1(matrix:list[list[int]]) -> None:
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = matrix[i][j]
            
    matrix[:] = rotated
    
    
    
# transpose and reverse - O(n²), O(1)
def rotate_image_2(matrix: list[list[int]]) -> None:
    n = len(matrix)
    
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    


if __name__ == "__main__":
    loop = int(input())
    
    for _ in range(loop):
        n = int(input())
        
        matrix = []
        for i in range(n):
            temp = list(map(int, input().split()))
            matrix.append(temp)
            
        # rotate_image_1(matrix)
        rotate_image_2(matrix)
        
        print(matrix, end='\n\n')
        
        
'''
5
3
1 2 3
4 5 6
7 8 9
4
5 1 9 11
2 4 8 10
13 3 6 7
15 14 12 16
4 
13 20 31 34
42 51 64 62
72 81 93 89
-40 -81 -93 -89
3
-1 -2 -3
0 5 -6
7 -8 9
3
0 2 -3
-4 5 6
7 -8 9
'''