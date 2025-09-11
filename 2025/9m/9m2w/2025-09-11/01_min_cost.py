#   A  B  C  공장
# 1 73 21 21
# 2 11 59 40
# 3 24 31 83
#제품

import sys
sys.stdin = open("min_cost_input.txt", "r")
sys.stdout = open("min_cost_output.txt", "w") 

T = int(input())

def check_matrix(row, col):
    is_posible = True

    # 같은 열에 놓은 것이 있는지
    for i in range(row):
        if visited[i][col]:
            is_posible = False

    return is_posible

def solve(row, current_cost):
    global result

    # 0. 가지치기(Pruning)
    if current_cost >= result:
        return

    # 1. 종료 조건
    if row == N:
        result = min(result, current_cost)
        return

    # 2. 재귀 호출
    for col in range(N):
        # 행 기준 안겹친다면
        if not visited[col]:
            visited[col] = True
            solve(row + 1, current_cost + V[row][col])
            visited[col] = False

    

for tc in range(1, T+1):
    # 제품의 수
    N = int(input())
    # 공장별 생산 비용
    V = [list(map(int, input().split())) for _ in range(N)]
    # 방문 배열
    visited = [False] * N

    result = float("inf")

    solve(0, 0)

    print(f"#{tc} {result}")