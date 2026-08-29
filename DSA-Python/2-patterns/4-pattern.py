'''
1
22
333
4444
55555
'''


def main(n:int) -> None:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(i, end='')
            
        print()
        
        
if __name__ == "__main__":
    n = int(input())
    
    main(n)