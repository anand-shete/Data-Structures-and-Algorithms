'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''


def main(n:int) -> None:
    cnt = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(cnt, end=' ')
            cnt += 1
    
        print()
        
        
if __name__ == "__main__": 
    n = int(input())
    main(n)