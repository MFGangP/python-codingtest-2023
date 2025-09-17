import sys
import heapq
sys.stdin = open("MST_input.txt", "r")

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(y, x):
    king_x = find_set(x)
    king_y = find_set(y)

    # 대표 노드가 같으면 순회 생김
    if king_x == king_y:
        return 
    
    parent[king_x] = king_y

T = int(input())

for tc in range(1, T+1):
    # 노드 번호 V
    # 간선의 개수 E
    V, E = map(int, input().split())

    edge_count = 0
    min_weight = 0
    
    edges = []
    # 간선의 개수 E만큼 값을 받음
    for _ in range(E):
        # n1, n2, 가중치 w
        n1, n2, w = list(map(int, input().split()))
        # n1에서 n2로 가는 w의 가중치를 가진 간선의 정보
        edges.append((n1, n2, w))

    edges.sort(key=lambda x : x[2])

    parent = [i for i in range(V + 1)]

    # 모든 간선을 확인
    for s, e, w in edges:
        # 두 정점의 대표가 다를 때만 (사이클을 만들지 않을 때만)
        if find_set(s) != find_set(e):
            # 간선을 선택하고 두 집합을 합침
            union(s, e)
            edge_count += 1
            min_weight += w

            # MST가 완성되면 (V-1개의 간선을 선택하면) 종료
            if edge_count == V + 1: # 0번부터 V번까지 V + 1개의 정점
                break

    print(f"#{tc} {min_weight}")