import sys
sys.stdin = open("dessert_cafe_input.txt", "r")
sys.stdout = open("dessert_cafe_output.txt", "w")

# 우하, 좌하, 좌상, 우상,
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def solve(i, j, direction, dessert_list):
    global max_desserts
    
    # [재귀 호출]
    # 선택지 1: 현재 방향으로 직진
    # 선택지 2: 다음 방향으로 회전 (단, direction < 3)
    # 두 선택지를 모두 탐색해야 하므로, direction부터 3까지 반복할 수 있습니다.
    # 하지만 더 간단하게는, 현재 방향(d)과 다음 방향(d+1) 두 가지만 고려하면 됩니다.
    
    # d는 현재 방향(direction) 또는 다음 방향(direction+1)이 될 수 있음
    for d in range(direction, direction + 2):
        # 방향은 3(우상)을 넘어설 수 없음
        if d > 3:
            continue

        ni = i + di[d]
        nj = j + dj[d]
        
        # 1. [종료 조건] 다음 위치가 출발점인가?
        # 방향 전환을 3번 모두 마친 상태(d==3)에서만 유효한 종료
        if ni == start_i and nj == start_j and d == 3:
            # 성공! 디저트 개수를 세고 최대값 갱신
            max_desserts = max(max_desserts, len(dessert_list))
            return

        # 2. [탐색 계속] 다음 위치가 유효한 경로인가?
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] not in dessert_list:
            dessert_list.append(matrix[ni][nj])
            solve(ni, nj, d, dessert_list)
            dessert_list.pop()

T = int(input())

for tc in range(1, T+1):
    # NxN 배열 크기
    N = int(input())

    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 일단 없다 가정하고 변수 생성
    max_desserts = -1
        
    for i in range(N):
        for j in range(N):
            start_i, start_j = i, j
            solve(i, j, 0, [matrix[i][j]])

    print(f"#{tc} {max_desserts}")