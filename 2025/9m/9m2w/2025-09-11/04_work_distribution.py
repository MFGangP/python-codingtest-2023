import sys
sys.stdin = open("work_distribution_input.txt", "r")
sys.stdout = open("work_distribution_output.txt", "w")

def solve(row, current_value):
    global result

    # 1. 가지치기
    if current_value <= result:
        return

    # 2. 종료 조건
    if row == N:
        result = current_value
        return

    # 3. 재귀
    for col in range(N):
        # col번째 일이 아직 배분되지 않았다면
        if not visited[col]:
            visited[col] = True
            # 현재 확률을 곱해서 넘겨줌
            solve(row + 1, current_value * (P[row][col] / 100))
            visited[col] = False

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    result = 0.0

    solve(0, 1.0)

    print(f"#{tc} {result * 100:.6f}")