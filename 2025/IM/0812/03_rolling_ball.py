# 상하좌우 이동 O => 델타 사용
import sys
sys.stdin = open("rolling_ball_input.txt", mode='r')
sys.stdout = open("rolling_ball_output.txt", mode='w') 

# 
def dfs(x, y):
    # 1. 가장 작은 이웃을 찾을 변수를 초기화.
    # 갈 곳이 없는 경우를 대비해 None으로 초기화.
    next_x, next_y = None, None
    min_neighbor_value = 100  # 문제의 최대값인 99보다 큰 100으로 초기화

    # 2. 상하좌우 모든 이웃을 탐색.
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy

        # 3. 이웃이 유효한 범위에 있는지 .
        if 0 <= nx < N and 0 <= ny < N:
            # 4. 이웃이 현재 칸보다 작고, 지금까지 찾은 가장 작은 이웃보다도 작으면
            if array[nx][ny] < array[x][y] and array[nx][ny] < min_neighbor_value:
                # 5. 가장 작은 이웃 정보를 업데이트.
                min_neighbor_value = array[nx][ny]
                next_x, next_y = nx, ny

    # 6. 모든 이웃을 탐색한 후, 이동할 곳이 있는지 확인.
    if next_x is not None:
        # 이동할 곳이 있다면, 1(현재 칸) + 재귀 호출 결과(다음 칸부터의 이동 횟수)를 반환.
        return 1 + dfs(next_x, next_y)
    else:
        # 이동할 곳이 없다면, 현재 칸의 횟수 1만 반환.
        return 1
        
T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    # N x N 배열
    array = [list(map(int, input().split())) for _ in range(N)]
    # 최대 이동 횟수
    max_count = 0
    # 탐색을 시작할 좌표
    # 이동 방향은 상 하 좌 우
    for i in range(N):
        for j in range(N):
            # 특정 좌표에서 이동한 횟수
            move_count = dfs(i, j)

            if max_count < move_count:
                max_count = move_count

    print(f"#{testcase} {max_count}")