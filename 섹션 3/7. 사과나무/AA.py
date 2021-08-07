import sys

# sys.stdin = open("in1.txt", "rt")

n = int(input())
result = 0
for i in range(n):
    row = list(map(int, input().split()))

    mid = n // 2
    if i <= mid:
        result += sum(row[mid - i:n - (mid - i)])
    else:
        result += sum(row[i - mid:n - (i - mid)])

print(result)
