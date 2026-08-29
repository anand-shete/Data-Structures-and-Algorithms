'''
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
'''

def main(n:int) -> None:
    for i in range(1, n+1):
        for j in range(n, i, -1):
            print(end=' ')
            
        for j in range(1, 2*i):
            print('*', end='')
            
        print()
        
    for i in range(n, 0, -1):
        for j in range(0, n-i):
            print(end=' ')
        
        for j in range(1, 2*i):
            print('*', end='')
        print()    
        

if __name__ == "__main__":
    n = int(input())
    
    main(n)