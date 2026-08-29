def main():
    # input() takes single line as input
    n = str(input())
    print('single string:',n)
    print()


    n  = int(input())
    print('single integer:', n)
    print()
    

    # multiple strings on single line
    a, b, c = input().split()
    print("string1:",a)
    print("string2:",b)
    print("string3:",c)
    print()
    
    
    # multiple integers single line
    a,b,*rest = map(int, input().split())
    print('a:',a)
    print('b:',b)
    print('rest:',rest)
    print()
    
    
    # list
    nums = list(map(int, input().split()))
    print(nums)
    print()
    
    
    # each input on new line
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(int(input()))
    print(nums)
    print()
    
    
    # 2d matrix
    rows, cols = map(int, input().split())
    matrix = []
    for i in range(rows):
        row_list = list(map(int, input().split()))
        matrix.append(row_list)
    print(matrix)
    
    
if __name__ == "__main__":
    main()
