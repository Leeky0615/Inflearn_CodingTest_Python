import sys

# sys.stdin = open("in1.txt", "rt")

L = int(input())
boxes = sorted(list(map(int, input().split())))
M = int(input())

for _ in range(M):
    boxes[0] += 1
    boxes[L-1] -= 1
    boxes.sort()

print(boxes[L-1]-boxes[0])