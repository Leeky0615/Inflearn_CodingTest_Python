import sys

# sys.stdin = open("in1.txt", "rt")
n, m = map(int, input().split())
result = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        result[i + j] += 1

max = max(result)

for idx, x in enumerate(result):
    if x == max:
        print(idx, end=' ')
