import sys

# sys.stdin = open("in3.txt", "r")

arr = [list(map(int, input().split())) for _ in range(9)]


def sudoku():
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            duplicated = [True] * 9
            for k in range(9):
                val = arr[i + k // 3][j + k % 3]
                if not duplicated[val - 1]:
                    return "NO"
                duplicated[val - 1] = False
    else:
        return "YES"


print(sudoku())
