'''
    A
   ABA
  ABCBA
 ABCDCBA
ABCDEDCBA
'''


def main(n:int) -> None:
    for i in range(1, n+1):
        for j in range(n-i, 0, -1):
            print(end=' ')
        
        for j in range(65, 65+i):
            print(chr(j), end='')
            
        for j in range(1, i):
            print(chr(i-j+64), end='')
        print()
    
    
if __name__ == "__main__": 
    n = int(input())
    main(n)