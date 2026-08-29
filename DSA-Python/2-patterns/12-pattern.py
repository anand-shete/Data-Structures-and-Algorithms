'''
1        1
12      21
123    321
1234  4321
1234554321
'''

def main(n:int) -> None:
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end='')
        
        for j in range(2*(n-i), 0, -1):
            print(end=' ')
            
        for j in range(i, 0, -1):
            print(j, end='')
        print()
        

if __name__ == "__main__":
    n = int(input())
    
    main(n)