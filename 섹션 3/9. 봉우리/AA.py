import sys

sys.stdin = open("in1.txt", "r")

# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [[True] * n for _ in range(n)]
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
# count = 0
# for y in range(n):
#     for x in range(n):
#         if visited[y][x]:
#             status = True
#             for k in range(4):
#                 nx = x + dx[k]
#                 ny = y + dy[k]
#                 if 0 <= nx < n and 0 <= ny < n:
#                     if arr[ny][nx] < arr[y][x]:
#                         visited[ny][nx] = False
#                     else:
#                         status = False
#             if status:
#                 count += 1
#
# print(count)

n = int(input())
arr = [[0] * (n + 2) for i in range(n + 2)]
for i in range(1, n + 1):
    arr[i][1:n + 1] = list(map(int, input().split()))
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(arr[i][j] > arr[i+dx[k]][j+dy[k]] for k in range(4)):
            count +=1

print(count)