'''
A
AB
ABC
ABCD
ABCDE
'''

def main(n:int)-> None:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(chr(64+j), end='')
            
        print()

if __name__ == "__main__": 
    n = int(input())
    main(n)