'''
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
'''

def main(n:int) -> None:
    for i in range(1, n+1):
        
        for j in range(0, i):
            print((i+j) % 2, end=' ')
            
        print()

if __name__ == "__main__":
    n = int(input())
    
    main(n)