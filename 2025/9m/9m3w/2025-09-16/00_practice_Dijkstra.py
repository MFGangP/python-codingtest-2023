# 위상정렬
# 플루이드 워셜 - 3중 반복 무식한 방법
# A*
# 벨만 포드

import heapq

# start : 시작 정점
# start 정점에서 시작해서 다른 모든 정점까지 가는데 최단 거리를 구한다.
def dijkstra(start):
    # 힙을 사용하는 이유
    # 우리는 가중치가 가장 작은 간선을 선택 => 최소합
    heap = []

    # 초기 상태에서 시작 정점 처리
    # (0, 시작 정점)
    heapq.heappush(heap, (0, start))

    # D
    # D[i] = 시작 정점에서 i번 정점 까지의 최단 거리
    INF = float("inf")
    # 처음 계산하기 전에는 무한대다.
    D = [INF] * V
    # 시작 정점에서 시작 정점까지 거리는 0이다
    D[start] = 0

    # 힙에 간선 정보가 남아있지 않을 때 까지 반복
    while heap:
        # 다음에 도착 가능한 정점 중에 간선의 가중치가 최소가 되는 정점을 선택
        # heap에서 하나 꺼내오기만 하면 (최소 가중치, 정점 번호) 꺼내오기 가능
        w, v = heapq.heappop(heap)

        # v를 이전에 선택한 적이 있다면 건너뛰어야한다.
        # v까지 가는 경우의 수는 여러개가 있을 수 있다.
        # 10, 20, 30 이라는 경우의 수가 있다면
        # 그 중 가장 먼저 꺼내지는 값은 10이기 때문에
        # 이후에 나오는 다른 값들은 볼 필요가 없는 것
        if w > D[v]:
            continue

        # v를 선택, v를 거쳐서 갈 수 있는 다른 새로운 길 계산
        # 이 새로운 길의 가중치가 내가 이전에 계산한 가중치보다 작으면 갱신
        
        # v와 인접한 정점을 조사
        # nv : v와 인접한 정점번호, nw : 그때 가중치
        for nv, nw in g[v]:
            # v를 거쳐서 nv로 가는 새로운 길을 발견!
            # 그때의 거리 = v까지의 최단 거리 + v-nv까지의 거리
            new_distance = w + nw

            # 이 새로 계산한 거리가 이전에 계산한 거리보다 작나?
            # 이전에도 nv에 다른 경로로 도착한 적이 있을수 있는데
            # 그때의 값을 v를 거쳐 nv로 가는 값과 비교해서 작은 값으로 갱신
            # new_distance < D[nv] 
            if new_distance < D[nv]:
                D[nv] = new_distance
                # D[nv] 까지의 최단 거리가 갱신되었으므로
                # NV 까지의 최단거리를 힙에 추가
                heapq.heappush(heap, (new_distance, nv))
    
# V : 정점 개수
# E : 간선 개수
V, E = map(int, input().split())

# 인접 행렬 / 인접 리스트
# g[i] = [(i 번 정점과 연결되어 있는 정점 번호, 가중치), ..]
g = [[] for _ in range(V)]

for _ in range(E):
    # s에서 e로 가는 간선의 가중치 w
    s, e, w = map(int, input().split())
    # s에서 갈 수 있는 정점의 가중치 추가
    g[s].append((e, w))

dijkstra(0)

print()