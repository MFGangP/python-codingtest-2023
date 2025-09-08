from collections import deque
import sys
sys.stdin = open("node_range_input.txt", "r")
sys.stdout = open("node_range_output.txt", "w")

T = int(input())

def bfs(S, G):
    # 초기화
    # visited 생성
    visited = [0] * ( V + 1 )
    # 큐 생성
    # 시작점 인큐
    que = deque()
    que.append(S)
    # 시작점 인큐 표시
    visited[S] = 1

    # 반복
    # 탐색할 정점이 남아 있으면
    while que:
        # 디큐
        v = que.popleft()
        # visit()
        # 디큐 한 값이 목적지라면
        if v == G:
            # 방문 횟수 리턴
            return visited[v]-1
        
        # v와 인접한 정점을 탐색, 갈 수 있는 정점이면
        # 큐를 통해 방문 예약
        for nv in range(1,V+1):
            # v에서 nv번 정점으로 갈수 있다.
            # 1. adj_m[v][nv] == 1 : v에서 nv로 가는길이 있다.
            # 2. visited[nv] == 0 : nv를 방문한적이 없다.
            if nodes[v][nv] == 1 and not visited[nv]:
                # nv는 방문예정입니다. 라는 사실을 큐에 저장
                que.append(nv)
                # nv 방문 체크까지
                # nv 까지의 거리 = v까지의 거리 + 1
                visited[nv] = visited[v] + 1
    return 0

for testcase in range(1, T+1):
    # V개의 노드 개수와 
    # 방향성이 없는 E개의 간선 정보
    V, E = map(int, input().split())
    nodes = [[0] * (V + 1) for _ in range(V + 1)] # V번 행까지 준비
    # 좌표 정보 등록
    for i in range(E):
        # 출발 노드 s와 도착 노드 g
        s, g = map(int, input().split())    
        # 인접 행렬 
        nodes[s][g] = 1
        nodes[g][s] = 1
    # 시작 노드 , 끝 노드
    S, G = map(int, input().split())
    result = bfs(S, G)
    print(f"#{testcase} {result}")