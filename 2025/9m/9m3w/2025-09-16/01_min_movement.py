from heapq import heappop, heappush
import sys

sys.stdin = open("min_movement_input.txt", "r")


def dijkstra(start):
    # 정점계산을 위한 heap 선언
    heap = []
    # 시작 정점 heap에 추가
    heappush(heap, (0, start))

    # heap에 값이 있는 동안 계속
    while heap:
        # heap에서 꺼내오는 값이 가중치가 가장 작은 값이 나오게 되어있다.
        w, v = heappop(heap)
        # 이전에 가중치가 작은 값이 이미 들어가있으면 볼 필요 없다.
        if w > D[v]:
            continue

        # 인접 리스트에서 v와 연결된 값들을 꺼내보기
        for nv, nw in g[v]:
            new_distance = w + nw
            # nv에 저장되어있는 가중치가 새로운 가중치보다 클 경우
            if D[nv] > new_distance:
                # 값을 갱신해준다.
                D[nv] = new_distance
                # 값이 갱신됐으니까 다시 heap에 넣어준다.
                heappush(heap, (new_distance, nv))


T = int(input())

for tc in range(1, T + 1):
    # N : 정점의 개수
    # E : 간선의 개수
    N, E = map(int, input().split())

    INF = float("inf")

    # g[] - 인접 리스트 i와 연결되어있는 정점들의 모음
    g = [[] for _ in range(E)]
    # 방문 여부 및 최소 가중치를 위한 리스트
    D = [INF] * E
    # 시작 정점을 위해 0을 넣어준다.
    D[0] = 0

    for i in range(E):
        # 시작 정점, 목표 정점, 가중치
        s, e, w = map(int, input().split())
        # 인접 리스트에 도착 정점과 가중치를 입력
        g[s].append((e, w))

    dijkstra(0)

    print(f"#{tc} {D[N]}")
