'''
*****

*   *

*   *

*   *

*****
'''


def main(n:int) -> None:
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1 or i == n:
                print('*', end='')
            elif j == 1 or j == n:
                print('*', end='')
            else:
                print(end=' ')
        print('\n')
        

if __name__ == "__main__": 
    n = int(input())
    main(n)