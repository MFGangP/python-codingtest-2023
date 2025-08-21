import sys
sys.stdin = open("stone_flipping_game_1_input.txt", mode='r')
sys.stdout = open("stone_flipping_game_1_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())
    Default_N = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        base_color = Default_N[i-1]  # i번째 돌의 색
        for x in range(j):           # j개의 돌 바꾸기
            if i-1+x < N:            # 범위 안일 때만
                Default_N[i-1+x] = base_color

    print(f"#{testcase}", *Default_N)
