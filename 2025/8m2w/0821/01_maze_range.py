import sys
from collections import deque

sys.stdin = open("maze_range_input.txt", "r")
sys.stdout = open("maze_range_output.txt", "w")

T = int(input())
# 시작점 찾기
def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j        
# 도착점 찾기
def bfs(i, j, N):
    # visited 생성
    visited = [[0] * N for _ in range(N)]
    # 큐 생성, 시작점 인큐
    que = deque()
    que.append([i, j])
    # 인큐 표시
    visited[i][j] = 1
    # 반복
    while que:
        # 디큐
        ti, tj = que.popleft()
        # 방문해서 할 일 => 현재 방문한 정점 i,j
        # maze의 i,j가 3이면 => 여기가 목적지니?
        if maze[ti][tj] == 3:
            # 도착지 visited 값에서 -1 한 값을 반환
            return visited[ti][tj] - 1 -1 # 경로의 빈칸 수, -1 추가
        # 방문 정점에 인접하고 미방문이면
        # 인접 = 상하좌우 중에 벽이 아니어야 한다.
        # 미방문 = visited가 0인 경우
        # 상 하 좌 우
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]
        for x in range(4):
            wi, wj = ti + di[x], tj + dj[x]
            if 0<=wi<N and 0<=wj<N and maze[wi][wj]!=1 and visited[wi][wj] == 0:
                # 인큐
                que.append([wi, wj])
                # 인큐 표시
                visited[wi][wj] = visited[ti][tj] + 1
    return 0

for testcase in range(1, T+1):
    
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    # 시작 점 찾기
    i , j = find_start(N)
    # 도착 점 찾기
    ans = bfs(i, j, N)
    print(f"#{testcase} {ans}")