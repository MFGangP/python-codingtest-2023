# 백준 1920번 - 원하는 정수 찾기

N = int(input()) # 5
A = list(map(int,input().split())) # 4 1 5 2 3
A.sort() # 파이썬 리스트에서 제공하는 기본 정렬
M = int(input())
target_list = list(map(int,input().split())) # 1 3 7 9
# 찾아야할 데이터 리스트

for i in range(M):
    find = False # 검색 여부 기본값
    target = target_list[i]
    start = 0
    end = N - 1 # len(A) - 1

    while start <= end:
        midle = (start + end) // 2 # 중앙 인덱스 값
        midv = A[midle] # 중앙에 있는 값
        if midv > target:   # 오른쪽 값 무시
            end = midle - 1
        elif midv < target: # 왼쪽 값 무시
            start = midle + 1
        else:               # 값 찾음
            find = True
            break
    if find:
        print(1)
    else:
        print(0)