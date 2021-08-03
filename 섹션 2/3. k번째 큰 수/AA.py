import sys
from itertools import combinations

# sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split())
arr = list(map(int, input().split()))
res = sorted({sum(i) for i in combinations(arr, 3)}, reverse=True)
print(res[k - 1])
