import sys

sys.stdin = open("kill_fly_3_input.txt", mode='r')
sys.stdout = open("kill_fly_3_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):
    # N = 배열 크기
    # M = 퇴치 크기
    N, M = list(map(int, input().split()))

    # N x N으로 이루어진 2차원 배열
    array = [list(map(int, input().split())) for _ in range(N)]

    max_vaule = 0

    for i in range(N):
        for j in range(N):
            sum_value = array[i][j]
            for di, dj in [[-1,0],[0,1],[1,0],[0,-1]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        sum_value += array[ni][nj]
            if max_vaule < sum_value:
                max_vaule = sum_value

    for i in range(N):
        for j in range(N):
            sum_value = array[i][j]
            for di, dj in [[1,1],[-1,1],[1,-1],[-1,-1]]:
                for c in range(1, M):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        sum_value += array[ni][nj]
            if max_vaule < sum_value:
                max_vaule = sum_value
                
    print(f"#{time} {max_vaule}")