from math import sqrt
import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())

arr = [False, False] + [True] * (n - 1)
cnt = 0
for i in range(2, int(sqrt(n)) + 1):
    if arr[i]:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1

print(arr.count(True))
