import sys

sys.stdin = open("in1.txt", mode='r')

sys.stdout = open("out1.txt", mode='w')

T = int(input())

for time in range(1, T+1):
    # N = 배열 크기
    # M = 이동 하는 칸의 크기
    N, M = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0
    for i in range(N):
        for j in range(N):
            s = x = matrix[i][j] # M, M를 중심으로
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 각 진행 방향
                for c in range(1, M): # 거리별 - 한칸 뻗어나갔을 때의 값을 나타냄 
                # 0부터 시작하면 나 자신을 포함하게 되버려서 총 4번 더함
                    ni, nj = i+di*c, j+dj*c
                    # 한 방향으로 뻗어나감
                    if 0<=ni<N and 0<=nj<N:
                        s += matrix[ni][nj]
            for di, dj in [[1,1],[1,-1],[-1,-1],[-1,1]]: # 각 진행 방향
                for c in range(1, M): # 거리별 - 한칸 뻗어나갔을 때의 값을 나타냄 
                # 0부터 시작하면 나 자신을 포함하게 되버려서 총 4번 더함
                    ni, nj = i+di*c, j+dj*c
                    # 한 방향으로 뻗어나감
                    if 0<=ni<N and 0<=nj<N:
                        x += matrix[ni][nj]
            if max_v < s:
                max_v = s
            if max_v < x:
                max_v = x
    print(f"#{time} {max_v}")