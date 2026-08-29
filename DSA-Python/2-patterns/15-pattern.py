'''
ABCDE
ABCD
ABC
AB
A
'''

def main(n:int)-> None:
    for i in range(n, 0, -1):
        for j in range(1, i+1):
            print(chr(64+j), end='')
            
        print()

if __name__ == "__main__": 
    n = int(input())
    main(n)