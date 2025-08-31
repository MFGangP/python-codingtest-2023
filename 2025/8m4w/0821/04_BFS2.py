from collections import deque

# 2차원 배열에서는 인접한 정점 => 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1]]

def is_vaild(i, j):
    return 0<=i<N and 0<=j<N

# si, sj : 시작 위치 좌표(si : 행번호, sj : 열번호)
def bfs(si, sj):
    # 중복체크
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 시작 위치 큐에 넣고
    q.append((si, sj))
    # 방문 위치 체크
    visited[si][sj] = 1

    # q 안에 탐색할 좌표가 남아있으면 계속
    while q:
        # 큐에서 다음 탐색 위치 꺼내오기
        i, j = q.popleft()

        # 이 꺼낸 위치(내가 방문하고 있는 위치) 도착점인지 판단
        if maze[i][j] == 99:
            # 탈출한 위치 거리 값 반환
            return visited[i][j]

        # 이 i, j와 인접한 상하좌우 방향 확인
        # 상하좌우에 방문할 곳이 있는지 판단
        for d in range(4):
            # 상하좌우로 1칸씩 이동한 좌표 계산
            ni, nj = i+di[d], j+dj[d]
            # 이동 후 좌표가 ni, nj 방문가능한 위치인가?
            # 1. ni, nj가 유효한 인덱스 범위 안인가
            # 2. 방문한 적이 없어야 한다.
            # 3. maze[ni][nj] != 벽(1)이 아니어야 이동 가능하다
            if is_vaild(ni, nj) and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                # 위의 3개의 조건을 만족하면 ni, nj는 방문가능한 위치
                # 큐에 다음에 방문할 것이다. 라고 예약
                q.append((ni, nj))
                # 중복 방지 + 거리 계산
                visited[ni][nj] = visited[i][j] + 1

    # while 문 종료 후 코드가 여기까지 실행 되었다.
    # 중간에 우리가 찾는 목표 지점을 찾지 못했다.
    return -1