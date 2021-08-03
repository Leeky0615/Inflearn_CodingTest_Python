import sys

# sys.stdin = open("in1.txt", "rt")
t = int(input())
for i in range(t):
    print("#", i+1, sep='',end=' ')
    N, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sorted(arr[s - 1:e])[k-1])
