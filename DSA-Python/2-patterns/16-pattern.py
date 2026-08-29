'''
A
BB
CCC
DDDD
EEEEE
'''

def main(n:int)-> None:
    for i in range(n):
        for j in range(i+1):
            print(chr(65+i), end='')
            
        print()

if __name__ == "__main__": 
    n = int(input())
    main(n)