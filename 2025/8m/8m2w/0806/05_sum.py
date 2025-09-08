import sys
sys.stdin = open("sumin.txt", mode='r')
sys.stdout = open("sumout.txt", mode='w')

for time in range(1, 11):
    test_case = int(input())
    N = 100
    # 100x100 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_sum = 0

    for i in range(N):
        s = 0
        for j in range(N):
            s += matrix[i][j]
        if max_sum < s:
            max_sum = s

    for i in range(N):
        s = 0
        for j in range(N):
            s += matrix[j][i]
        if max_sum < s:
            max_sum = s  
    # 우상단 좌하단 
    s = 0
    for i in range(N):
        s += matrix[i][N - 1 - i]
    if max_sum < s:
        max_sum = s 
    # 좌상단 우하단 
    s = 0
    for i in range(N):
        s += matrix[i][i]
    if max_sum < s:
        max_sum = s 
    print(f"#{test_case} {max_sum}")
