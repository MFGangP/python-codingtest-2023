# V + 1 주의!
# 행렬이 아니라 그래프로 생각해보면 된다. 상하좌우 좌표만 신경쓰면 된다.
# 출발 왼쪽 위 도착 오른쪽 아래 
# 거리 - 가중치 최소 - kruskal

import sys
import heapq
sys.stdin = open("min_cost_input.txt", "r")

# 상하좌우 이동을 위한 방향 벡터
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dijkstra():
    # 우선순위 큐(최소 힙) 준비
    heap = []
    
    # D[i][j]: (0,0)에서 (i,j)까지 가는 데 필요한 최소 거리
    INF = float('inf')
    distance_cost = [[INF] * N for _ in range(N)]

    # 시작점 (0,0) 처리
    distance_cost[0][0] = 0
    # 힙에는 (누적 거리, 행, 열) 순서로 저장
    heapq.heappush(heap, (0, 0, 0))

    while heap:
        # 현재까지 누적 거리가 가장 적은 지점을 꺼냄
        current_distance, x, y = heapq.heappop(heap)

        # 이미 더 적은 거리로 도착한 경로가 있다면 건너뜀
        if current_distance > distance_cost[x][y]:
            continue

        # 현재 지점 (x,y)에서 상하좌우 이웃 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 맵 범위를 벗어나지 않는지 확인
            if 0 <= nx < N and 0 <= ny < N:
                # 다음 지점으로 이동하는 데 드는 추가 거리 계산
                move_cost = 1 # 기본 거리 1
                if H[nx][ny] > H[x][y]: # 오르막길이라면
                    move_cost += H[nx][ny] - H[x][y]
                
                new_distance = current_distance + move_cost

                # 새로운 경로가 기존 경로보다 더 저렴하다면
                if new_distance < distance_cost[nx][ny]:
                    # 최소 거리 갱신
                    distance_cost[nx][ny] = new_distance
                    # 힙에 새로운 경로 추가
                    heapq.heappush(heap, (new_distance, nx, ny))
    
    # 도착지(N-1, N-1)까지의 최소 거리 반환
    return distance_cost[N-1][N-1]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # H: 지역의 높이 정보 (2차원 배열)
    H = [list(map(int, input().split())) for _ in range(N)]
    
    result = dijkstra()
    
    print(f"#{tc} {result}")