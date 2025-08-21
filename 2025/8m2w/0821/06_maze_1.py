from collections import deque 
import sys

sys.stdin = open("maze_1_input.txt", "r")
sys.stdout = open("maze_1_output.txt", "w")

# 배열 크기
N = 16

# 출발점
Si, Sj = 1, 1
# 도착점
Gi, Gj = 13, 13

def is_vaild(ni, nj):
    return 0<=ni<N and 0<=nj<N

def bfs():
    # 큐 선언
    q = deque()
    # 시작점 삽입
    q.append((Si, Sj))

    # 방문 배열 선언
    visited = [[0] * N for _ in range(N)]

    # 큐 안에 값이 있다면 반복
    while q:
        # 좌표 꺼내기
        i, j = q.popleft()

        # 델타
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        for d in range(4):
            ni, nj = i+di[d], j+dj[d]
            # ni,nj가 범위 안이고 
            # 다음 목적지에 방문한 적이 없고 
            # 벽이 아니라면
            if is_vaild(ni, nj) and visited[ni][nj] == 0 and array[ni][nj] != 1:
                if array[ni][nj] == 3:
                    return 1
                # 큐에 방문 할 거라고 예약
                q.append([ni, nj])
                visited[i][j] = 1
    return 0

for _ in range(1, 11):
    # 테스트 케이스 입력
    T = int(input())

    # NxN 배열
    array = [list(map(int, input())) for _ in range(N)]

    result = bfs()

    print(f"#{T} {result}")