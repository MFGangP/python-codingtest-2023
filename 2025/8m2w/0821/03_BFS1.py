from collections import deque

"""
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
"""


# s : 탐색 시작 정점 번호
def bfs1(s):
    # 방문 배열
    # 중복방문체크 + 거리계산
    visited = [0] * (V + 1)

    # 큐
    # 내가 다음에 방문할 곳(예약)
    q = deque()

    # 시작 정점을 큐에 넣고 탐색
    q.append(s)
    # s는 방문했다 체크
    visited[s] = 1

    # 큐안에 방문할 곳이 남아있다면, 탐색 계속
    while q:
        # 큐에서 다음 방문할곳 하나 꺼내오기
        v = q.popleft()

        print(v, end=" ")

        # v와 인접한 정점을 탐색, 갈 수 있는 정점이면
        # 큐를 통해 방문 예약
        for nv in range(1,V+1):
            # v에서 nv번 정점으로 갈수 있다.
            # 1. adj_m[v][nv] == 1 : v에서 nv로 가는길이 있다.
            # 2. visited[nv] == 0 : nv를 방문한적이 없다.
            if adj_m[v][nv] == 1 and not visited[nv]:
                # nv는 방문예정입니다. 라는 사실을 큐에 저장
                q.append(nv)
                # nv 방문 체크까지
                # nv 까지의 거리 = v까지의 거리 + 1
                visited[nv] = visited[v] + 1

# s : 탐색 시작 정점 번호
def bfs2(s):
    # 방문 배열
    # 중복방문체크 + 거리계산
    visited = [0] * (V + 1)

    # 큐
    # 내가 다음에 방문할 곳(예약)
    q = deque()

    # 시작 정점을 큐에 넣고 탐색
    q.append(s)
    # s는 방문했다 체크
    visited[s] = 1

    # 큐안에 방문할 곳이 남아있다면, 탐색 계속
    while q:
        # 큐에서 다음 방문할곳 하나 꺼내오기
        v = q.popleft()

        print(v, end=" ")

        # v와 인접한 정점을 탐색, 갈 수 있는 정점이면
        # 큐를 통해 방문 예약
        for nv in adj_l[v]:  # 인접 리스트는 v에서 갈수있는 정점만 들어있다.
            # v에서 nv번 정점으로 갈수 있다.
            # 1. visited[nv] == 0 : nv를 방문한적이 없다.
            if not visited[nv]:
                # nv는 방문예정입니다. 라는 사실을 큐에 저장
                q.append(nv)
                # nv 방문 체크까지
                # nv 까지의 거리 = v까지의 거리 + 1
                visited[nv] = visited[v] + 1

# 정점의 개수 : V
# 간선의 개수 : E
V, E = map(int, input().split())

# 인접 행렬
adj_m = [[0] * (V + 1) for _ in range(V + 1)]
# 인접 리스트
adj_l = [[] for _ in range(V + 1)]
# 그래프 정보가 한줄로 들어온다
graph = list(map(int, input().split()))

for i in range(E):
    s, e = graph[i * 2], graph[i * 2 + 1]

    # 인접행렬
    adj_m[s][e] = 1
    adj_m[e][s] = 1
    # 인접리스트
    adj_l[s].append(e)
    adj_l[e].append(s)

bfs2(1)