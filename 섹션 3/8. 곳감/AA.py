import sys

# sys.stdin = open("in1.txt", "rt")

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    row, direction, rotations = map(int, input().split())
    for i in range(rotations):
        if direction == 0:  # 맨 앞을 꺼내서 뒤로 보내기. -> 왼쪽 이동
            arr[row-1].append(arr[row-1].pop(0))
        else:  # 맨 뒤를 꺼내서 앞으로 보내기 -> 오른쪽 이동
            arr[row-1].insert(0, arr[row-1].pop())

result = 0
s = 0
e = n
for idx, row in enumerate(arr):
    result += sum(row[s:e])
    if idx < n // 2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(result)
