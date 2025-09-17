# V : 정점의 개수 (0번부터 시작하므로 V+1로 사용)
# E : 간선의 개수
V, E = map(int, input().split())

edges = []
for _ in range(E):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

# 가중치(w)를 기준으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

# make_set: 초기 집합의 대표는 자기 자신
parent = [i for i in range(V + 1)]

# x번 정점의 대표를 찾는 연산 (경로 압축 적용)
def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]
    
# x가 속한 집합과 y가 속한 집합을 합치는 연산
def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    # 두 대표가 같다면 이미 같은 집합 (사이클 발생)
    if root_x == root_y:
        return

    # 대표를 root_x로 통일
    parent[root_y] = root_x

# 선택한 간선 개수와 가중치 합
edge_count = 0
min_weight = 0

# 모든 간선을 확인
for s, e, w in edges:
    # 두 정점의 대표가 다를 때만 (사이클을 만들지 않을 때만)
    if find_set(s) != find_set(e):
        # 간선을 선택하고 두 집합을 합침
        union(s, e)
        edge_count += 1
        min_weight += w

        # MST가 완성되면 (V-1개의 간선을 선택하면) 종료
        if edge_count == V: # 0번부터 V-1번까지 V개의 정점일 경우 V-1
            break

print(f"최소 비용 : {min_weight}")