import sys

sys.stdin = open("input1.txt", mode='r')

sys.stdout = open("output1.txt", mode='w')

T = int(input())

for time in range(1, T+1):
    # N = 배열 크기
    # M = 이동 하는 칸의 크기
    N, M = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_v = 0
    for i in range(N):
        for j in range(M):
            s = 0
            for _ in range(matrix[i][j]):
                s += matrix[i][j]
                for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: # 각 진행 방향
                    ni, nj = i+di, j+dj
                    # 한 방향으로 뻗어나감
                    if 0<=ni<N and 0<=nj<N and matrix[ni][nj] != 0:
                        s += matrix[ni][nj]
            if max_v <= s:
                max_v += s
    print(f"#{time} {max_v}")