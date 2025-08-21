import sys
sys.stdin = open("balloon_pang_2_input.txt", "r")
sys.stdout = open("balloon_pang_2_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())

    max_value = 0
    # NxM 배열 선언
    array = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            add_value = array[i][j]
            # 상, 하, 좌, 우
            di = [-1, 1, 0, 0]
            dj = [0, 0, -1, 1]
            for x in range(4):
                ni, nj = i+di[x], j+dj[x]
                if 0<=ni<N and 0<=nj<M:
                    add_value += array[ni][nj]

            max_value = max(max_value, add_value)
    print(f"#{testcase} {max_value}")