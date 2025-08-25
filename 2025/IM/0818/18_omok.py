import sys
sys.stdin = open("omok_input.txt", "r")
sys.stdout = open("omok_output.txt", "w")

T = int(input())

# 네 방향 (→, ↓, ↘, ↗)
directions = [(0,1), (1,0), (1,1), (-1,1)]

for testcase in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    is_possible = False

    for i in range(N):
        for j in range(N):
            if board[i][j] == "o":
                for di, dj in directions:
                    cnt = 1
                    ni, nj = i, j
                    for _ in range(4):  # 이미 시작점 포함했으니 4칸만 더 보면 됨
                        ni += di
                        nj += dj
                        if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == "o":
                            cnt += 1
                        else:
                            break
                    if cnt >= 5:
                        is_possible = True
                        break
            if is_possible:
                break
        if is_possible:
            break

    print(f"#{testcase} {'YES' if is_possible else 'NO'}")
