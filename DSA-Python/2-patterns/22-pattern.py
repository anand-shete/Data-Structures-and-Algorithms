"""
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
"""


def main(n: int) -> None:
    for i in range(2 * n - 1):
        for j in range(2 * n - 1):
            top = i
            left = j
            btm = 2 * n - 2 - i
            right = 2 * n - 2 - j
            minDist = min(top, btm, right, left)

            print(n - minDist, end=" ")
        print()


if __name__ == "__main__":
    n = int(input())
    main(n)
