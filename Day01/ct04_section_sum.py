# 입력 속도를 개선! 단, 주피터 노트북에서는 실행 불가
import sys
input = sys.stdin.readline # 이 부분이 없으면 백준 시간 초과!

suNo, quizNo = tuple(map(int, input().split(' ')))
numbers = list(map(int, input().split()))
prefix_sum = [0]    # 중요! 배열 0번째 인덱스 핵심!
temp = 0

for i in range(suNo):
    temp += numbers[i]  # temp 5 9 12 14 15
    prefix_sum.append(temp)
    # [0, 5, 9, 12, 14, 15]

for j in range(quizNo):
    s, e = tuple(map(int, input().split()))
    print(prefix_sum[e] - prefix_sum[s - 1])