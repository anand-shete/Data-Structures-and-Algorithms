'''
E 
D E 
C D E 
B C D E 
A B C D E
'''


def main(n:int) -> None:
    for i in range(1, n+1):
        for j in range(n-i, n):
            print(chr(j+65), end=' ')
    
        print()
    
if __name__ == "__main__": 
    n = int(input())
    main(n)