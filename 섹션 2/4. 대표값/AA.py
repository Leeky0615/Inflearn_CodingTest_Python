'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세
요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높
은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''

import sys

# sys.stdin = open("in1.txt", "rt")
n = int(input())
arr = list(map(int, input().split()))
avg = int(sum(arr) / n + 0.5)
result = sorted(arr, key=lambda x: abs(x - avg))[0]
print(avg, arr.index(result) + 1)

# for문 할 때 enumerate 를 사용 하면 인덱스와 원소 값을 동시에 찾을 수 있음
