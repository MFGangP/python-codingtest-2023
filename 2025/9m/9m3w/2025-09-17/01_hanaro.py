# 환경 부담금 E * L^2 최소로 지불하며,
# N개의 모든 섬을 연결할 수 있는 교통 시스템을 설계
import sys
from heapq import heappop, heappush

sys.stdin = open("hanaro_input.txt", "r")


def prim(tax):
    heap = []
    # 시작 지점 힙에 넣기 (총 비용, 노드 번호)
    heappush(heap, (0, 0))
    # 방문 리스트
    visited = [0] * N
    # 최저 세율
    min_cost = 0

    # 최소 비용 저장 리스트
    dists = [float("inf")] * N
    dists[0] = 0

    while heap:
        # 힙에서 비용 노드 번호 꺼내기
        cost, node = heappop(heap)

        # 이전에 방문한 적 있는 노드라면
        if visited[node]:
            continue

        # 방문 처리
        visited[node] = 1

        min_cost += cost

        for next_node in range(N):
            if visited[next_node]:
                continue

            new_cost = (
                (x_list[next_node] - x_list[node]) ** 2
                + (y_list[next_node] - y_list[node]) ** 2
            ) * tax

            # 만약 새로운 비용이 기존 비용보다 작다면
            if new_cost < dists[next_node]:
                # 비용 교체
                dists[next_node] = new_cost
                heappush(heap, (new_cost, next_node))

    return round(min_cost)


T = int(input())

for tc in range(1, T + 1):
    # 섬의 개수
    N = int(input())

    x_list = list(map(int, input().split()))
    y_list = list(map(int, input().split()))

    # E : 환경 부담금
    E = float(input())

    # 최소로 지불 = prim, kruskal
    # prim = 정점 기준
    # kruskal = 간선 기준

    result = prim(E)

    print(f"#{tc} {result}")
