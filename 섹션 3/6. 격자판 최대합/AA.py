'''
5*5 격자판에 아래롸 같이 숫자가 적혀있습니다.
10 13 10 12 15
12 39 30 23 11
11 25 50 53 15
19 27 29 37 27
19 13 30 13 19
N*N의 격자판이 주어지면 각 행의 합, 각 열의 합, 두 대각선의 합 중 가 장 큰 합을 출력합
니다.
▣ 입력설명
첫 줄에 자연수 N이 주어진다.(1<=N<=50)
두 번째 줄부터 N줄에 걸쳐 각 줄에 N개의 자연수가 주어진다. 각 자연수는 100을 넘지 않는
다.
▣ 출력설명
최대합을 출력합니다.
'''
import sys

# sys.stdin = open("in1.txt", "rt")

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
rowSum = 0
colSum = 0
crossSum1 = 0
crossSum2 = 0
result = 0

for i in range(n):
    rowSum = 0
    colSum = 0
    for j in range(n):
        rowSum += arr[i][j]
        colSum += arr[j][i]

    crossSum1 = arr[i][i]
    crossSum2 = arr[i][n - i - 1]

    result = max(rowSum, colSum, crossSum1, crossSum2, result)

print(result)