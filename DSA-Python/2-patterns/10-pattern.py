'''
*
**
***
****
*****
****
***
**
*
'''

def main(n:int) -> None:
    for i in range(1, n+1):
        
        for j in range(0, i):
            print(end='*')
            
        print()
        
    for i in range(n-1, 0, -1):
        
        for j in range(i, 0, -1):
            print('*', end='')
            
        print()
        

if __name__ == "__main__":
    n = int(input())
    
    main(n)