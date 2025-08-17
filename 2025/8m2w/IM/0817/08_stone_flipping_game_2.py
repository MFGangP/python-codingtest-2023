import sys
sys.stdin = open("stone_flipping_game_2_input.txt", mode='r')
sys.stdout = open("stone_flipping_game_2_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    # N = 돌의 개수
    # M = 뒤집기 횟수
    N, M = map(int, input().split())

    Defalut_N = list(map(int, input().split()))

    # M 횟수 만큼 입력 받기
    for _ in range(M):
        # i 번째 돌을 사이에 두고
        # j 개의 돌 뒤집기
        i, j = map(int, input().split())
        for x in range(1, j+1):
            # 범위를 벗어나지 않았다면
            if i-x-1 >= 0 and i+x-1 < N:
                # 같은 색이면 뒤집고
                if Defalut_N[i-x-1] == Defalut_N[i+x-1]:
                    if Defalut_N[i-x-1] == 0:
                        Defalut_N[i-x-1] = Defalut_N[i+x-1] = 1
                    elif Defalut_N[i-x-1] == 1:
                        Defalut_N[i-x-1] = Defalut_N[i+x-1] = 0
                # 다른 색이면 그대로 둔다.
                else:
                    continue
    print(f"#{testcase}",*Defalut_N)