import sys
sys.stdin = open("n_queen_input.txt", "r")
sys.stdout = open("n_queen_output.txt", "w") 

T = int(input())

def check(row, col):
    is_posible = True
    # 같은 열에 있는지 확인
    x = row-1
    # x가 범위 안에 있는 동안 지속
    while x >= 0:
        # row, col 위에 퀸이 있다면
        if visited[x][col]:
            is_posible = False

    # 왼쪽 대각선에 있는지 확인
    i, j = row-1, col-1
    # i, j 가 범위 안에 있는 동안 지속
    while i >= 0 and j >= 0:
        # 왼쪽 대각선 위에 퀸이 있다면
        if visited[i][j]:
            is_posible = False

    # 오른쪽 대각선에 있는지 확인
    p, q = row-1, col+1
    # i, j 가 범위 안에 있는 동안 지속
    while p >= 0 and q >= 0:
        # 왼쪽 대각선 위에 퀸이 있다면
        if visited[p][q]:
            is_posible = False

    return is_posible

def solve(row):
    global result
    # 1. 탈출 조건

    # 끝까지 row가 도착했을 경우
    if row == N:
        result += 1
        return 
    
    # 2. 재귀
    for col in range(N):
        # 0. 가지치기 : 대각, 상단에 놓인게 있는지
        if check(row, col):
            visited[row][col] = 1
            solve(row+1)
            visited[row][col] = 0

for tc in range(1, T+1):
    # N 퀸 총 갯수
    result = 0
    # N : 보드 크기
    N = int(input())
    # NxN 체스판
    matrix = [[0] * N for _ in range(N)]
    # 방문 기록
    visited = [[0] * N for _ in range(N)]

    solve(0)

    print(f"#{tc} {result}")
