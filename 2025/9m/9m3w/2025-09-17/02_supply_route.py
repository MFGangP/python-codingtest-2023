# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 
# 총 복구 시간을 구하시오.
# 깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다
# 출발지는 좌상단의 칸(S)이고 도착지는 우하단의 칸(G)가 된다.
# S = (0, 0) G = (N-1, N-1)

# 상하좌우 = 델타
# 출발지에서 도착지까지 거리에 대해서는 고려할 필요가 없다.
# 다익스트라는 최소 거리 
# 출발지와 도착지를 제외한 곳이 0인 것은 복구 작업이 불필요한 곳

# 같은 줄에 빈 칸을 하나 두고, 주어진 입력에서 출발지에서 도착지까지 가는 경로 중에 
# 복구 작업에 드는 시간이 가장 작은 경로의 복구 시간을 출력
import sys
from heapq import heappop, heappush
sys.stdin = open("supply_route_input.txt", "r")

def dijkstra():
    # 거리 정보를 받을 2차원 배열
    dists = [[float("inf")] * N for _ in range(N)]
    dists[0][0] = 0

    # 누적거리, y, x
    heap = [(0, 0, 0)]

    while heap:
        # 좌표, 누적 거리 pop
        dist, j, i = heappop(heap)
        # 델타 시작
        for d in range(4):
            nj = j+dj[d]
            ni = i+di[d]

            # 범위 밖이면 다음 방향 확인
            if nj < 0 or nj >= N or ni < 0 or ni >= N:
                continue
            # 이때까지 누적 거리 + 다음 좌표의 거리
            new_dist = dist + graph[nj][ni]
                
            # 가지치기 이미 더 작은 값이 와있으면 패스
            if dists[nj][ni] <= new_dist:
                continue

            dists[nj][ni] = new_dist
            heappush(heap, (new_dist, nj, ni))

    return dists[N-1][N-1]

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]

T = int(input())

for tc in range(1, T+1):
    # 지도의 크기 : N
    N = int(input())
    # 지도 정보
    graph = [list(map(int, input())) for _ in range(N)] 

    result = dijkstra()

    print(f"#{tc} {result}")

