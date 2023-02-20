# 백준 10989

import sys
input = sys.stdin.readline
# 이건 기수정렬이 아니다. 계수 정렬
N = int(input()) # N 개 만큼 숫자를 받을거다
count = [0] * 10001 # 10000까지 할거라서 1 여유분

for i in range(N):  # N개 만큼 반복
    count[int(input())] += 1 # 입력한 숫자를 count[입력값]에 넣고 값 1 더하기

for i in range(10001): # 10001개 만큼 반복 
    if count[i] != 0: # 값이 0이 아니면(0이면 굳이 표시할 필요가 없음)
        for _ in range(count[i]): # 해당하는 숫자에 해당하는 인덱스 값 출력
            print(i)