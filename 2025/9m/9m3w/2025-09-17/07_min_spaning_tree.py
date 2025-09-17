def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

# union 연산
def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)
    
    # 대표가 같으면 순회가 생긴다.
    if king_x == king_y:
        return False
    
    # 두 집합을 합침
    parent[king_y] = king_x
    return True

T = int(input())
for tc in range(1, T + 1):
    # V: 정점의 개수, E: 간선의 개수
    V, E = map(int, input().split())
    
    # 모든 간선 정보를 저장할 리스트
    edges = []
    for _ in range(E):
        A, B, C = map(int, input().split())
        # (가중치, 정점1, 정점2)
        edges.append((C, A, B))
        
    # 가중치 기준으로 모든 간선 오름차순 정렬
    edges.sort()
    
    # 정점 번호 1~V
    parent = [i for i in range(V + 1)]
    
    total_weight = 0 # MST의 총 가중치
    edge_count = 0   # 선택된 간선의 수
    
    # 가중치가 낮은 간선부터 순회
    for weight, a, b in edges:
        # 사이클이 아니라면
        if union(a, b):
            # 간선을 MST에 포함
            total_weight += weight
            edge_count += 1
            
            # MST가 완성되면 종료
            if edge_count == V - 1:
                break
                
    print(f"#{tc} {total_weight}")