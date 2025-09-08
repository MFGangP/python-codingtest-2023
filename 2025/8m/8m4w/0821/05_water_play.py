from collections import deque
import sys

sys.stdin = open("water_play_input.txt", "r")
sys.stdout = open("water_play_output.txt", "w")

def is_vaild(i, j):
    return 0 <= i < N and 0 <= j < M

def bfs():
    # 큐를 초기화하고, 모든 물('W') 위치를 추가.
    q = deque()
    # 방문 기록 배열을 -1로 초기화하여 방문하지 않았음을 표시.
    # 만약 0으로 설정하고 아래 조건도 0으로 설정하면
    # W인 곳도 증가 시킴
    visited = [[-1] * M for _ in range(N)]

    # 모든 'W' 위치를 큐에 넣고, 거리를 0으로 초기화합니다.
    for i in range(N):
        for j in range(M):
            if array[i][j] == 'W':
                q.append((i, j))
                visited[i][j] = 0

    # 델타 배열 (상, 하, 좌, 우)
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]
    
    # BFS 탐색 시작
    while q:
        i, j = q.popleft()

        for d in range(4):
            ni, nj = i + di[d], j + dj[d]

            # 1. 유효한 범위 내에 있는지 확인
            # 2. 방문한 적이 없는지 확인
            if is_vaild(ni, nj) and visited[ni][nj] == -1:
                # 다음 칸의 거리를 현재 칸의 거리 + 1로 설정
                visited[ni][nj] = visited[i][j] + 1
                q.append((ni, nj))
    
    # 모든 육지 칸의 거리 합산
    total_sum = 0
    for i in range(N):
        for j in range(M):
            total_sum += visited[i][j]
            
    return total_sum

T = int(input())

for testcase in range(1, T + 1):
    N, M = map(int, input().split())
    array = [input() for _ in range(N)]
    
    result = bfs()

    print(f"#{testcase} {result}")