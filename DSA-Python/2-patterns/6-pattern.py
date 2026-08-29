'''
12345
1234
123
12
1
'''


def main(n:int) -> None:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(j, end='')
            
        print()
        
        
if __name__ == "__main__":
    n = int(input())
    
    main(n)