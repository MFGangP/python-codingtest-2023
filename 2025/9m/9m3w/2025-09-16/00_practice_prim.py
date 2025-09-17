"""
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
3 4 34
3 5 18
4 5 40
4 6 51
"""
# heapq에 가중치를 기준으로 원소를 삽입 또는 제거
from heapq import heappop, heappush

# 1. 임의의 정점을 하나 골라서 시작
# 2. 지금까지 내가 골랐던 정점들과 인접하는 정점 중에서 
#    최소 비용을 가진 간선을 선택 (이전에 선택한 적 없는 정점)
# 3. MST가 만들어질 때 까지 반복

def prim(start):
    # 우선순위 큐 (최소 힙)
    # 우선순위 큐가 가중치가 가장 작은 값을 넘겨준다.
    heap = []
    # MST[i] = 1 : i번 정점은 MST에 포함 (이전에 골랐다.)
    # MST[i] = 0 : i번 정점은 MST에 미포함 (이전에 고른적 없음)
    MST = [0] * V

    # 최소 비용
    min_w = 0

    # 힙에 시작 정점을 추가하고 반복 시작
    # (가중치, 정점 번호) 형태로 힙에 추가, 
    # 이때 힙의 우선순위 선정 기준은 튜플의 첫번째 원소
    # 시작 정점은 가중치 0
    heappush(heap, (0, start))
    # 정점을 선택한 횟수
    v_cnt = 0
    # 이때까지 선택한 정점의 개수가 V 보다 작으면 신장트리 완성 X
    # 큐 안에 뭔가 남아 있어야 남아있는 가중치 중에 작은거 선택
    while v_cnt < V and heap:
        # w : 가중치(힙 안에서 최소 였던)
        # v : 정점 번호
        w, v = heappop(heap)    
        # 이전에 방문한 적이 있는지 확인
        if MST[v]:
            # 건너뛰기 - 또 선택하면 순환이 생긴다
            continue
        
        # v가 이전에 선택한 적 없는 정점 번호라면 MST에 추가
        MST[v] = 1
        # 가중치의 합 누적
        min_w += w
        # 선택횟수 + 1
        v_cnt += 1

        # v를 새로 MST에 추가 했으니
        # v에서 새로 갈 수 있는 정점들의 정보도 heap에 추가
        for nv, nw in graph[v]:
            # nv : v에서 갈 수 있는 정점 번호
            # nw : 그 가중치

            # nv 정점을 이전에 고른적 있으면 건너뛴다.
            if MST[nv] == 1:
                continue

        # v에서 nv로 가는 간선 정보 추가
        # 이때 가중치는 nw
        heappush(heap, (nw, nv))

    # while이 종료되면 최소 신장 트리 완성
    return min_w

# V : 정점의 개수
# E : 간선의 개수
V, E = map(int, input().split())

graph = [[] for _ in range(V)] # 인접리스트

for i in range(E):
    s, e, w = map(int, input().split())

    graph[s].append((e, w))
    graph[e].append((s, w))

# 최소 신장트리의 가중치 합
print(f"최소 신장트리 가중치 합 : {prim(0)}")