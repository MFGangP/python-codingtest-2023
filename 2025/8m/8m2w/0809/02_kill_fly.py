import sys

sys.stdin = open("kill_fly_input.txt", mode='r')
sys.stdout = open("kill_fly_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):
    N, M = list(map(int, input().split()))

    # N x N으로 이루어진 2차원 배열
    array = [list(map(int, input().split())) for _ in range(N)]
    # 최대치 총합
    max_sum = 0

    # N x N - 가로 세로 N 칸으로 이루어진 배열
    # M x M 탐색을 해야해서 그만큼 빼줌.
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_value = 0
            # 탐색 할 M 칸의 상자
            for p in range(M):
                for g in range(M):
                    ni, nj = i+p, j+g
                    sum_value += array[ni][nj]
            if max_sum < sum_value:
                max_sum = sum_value           
    print(f"#{time} {max_sum}")


    #     # 현재 위치 값으로 값 선언
    # sum_array_value = array[i][j]
    # for di, dj in [[0, 1], [1, 0], [1, 1]]:
    #     for c in range(M):
    #         # 다음 i, j는 di, dj 만큼 이동한 값
    #         ni, nj = i+di*c, j+dj*c
    #         # 가려고 하는 좌표가 배열 크기를 넘지 않았자면
    #         if 0<=ni<N and 0<=nj<N:
    #             # 값을 더해준다.
    #             sum_array_value += array[ni][nj]
    # # 최대 값이 변했다면
    # if max_sum < sum_array_value:
    #     max_sum = sum_array_value