import sys
sys.stdin = open("kill_fly_3_input.txt", "r")
sys.stdout = open("kill_fly_3_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    # M은 파리약 뿌려지는 범위
    N, M = map(int, input().split())

    # N x N 배열
    array = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    # + 모양
    for i in range(N):
        for j in range(N):
            sum_value = array[i][j]
            # 상하좌우
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]
            for x in range(4):
                for c in range(1, M):
                    ni, nj = i+di[x]*c, j+dj[x]*c
                    if 0<=ni<N and 0<=nj<N:
                        sum_value += array[ni][nj]
            max_sum = max(max_sum, sum_value)

    # X 모양
    for i in range(N):
        for j in range(N):
            sum_value = array[i][j]
            # 좌상, 우하, 우상, 좌하
            di = [-1, 1, 1, -1]
            dj = [-1, 1, -1, 1]
            for x in range(4):
                for c in range(1, M):
                    ni, nj = i+di[x]*c, j+dj[x]*c
                    if 0<=ni<N and 0<=nj<N:
                        sum_value += array[ni][nj]
            max_sum = max(max_sum, sum_value)

    print(f"#{testcase} {max_sum}")