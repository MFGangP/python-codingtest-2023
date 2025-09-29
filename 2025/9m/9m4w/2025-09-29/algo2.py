T = int(input())

# 싸이클이 생기는지 체크
def find_set(x):
    # 싸이클이 만들어지면 안되니까 탈출
    if x == G[x]:
        return G[x]
    # 대표 정점 찾을 때 까지
    return find_set(G[x])

# 대표 노드 선정
def union(x, y):
    king_x = find_set(x)
    king_y = find_set(y)
    # 사이클이 만들어지면 안되니까 종료
    if king_x == king_y:
        # union 실패
        return False
    # 만약 서로 대표 노드가 다르다면, 동일한 대표 노드 만들어주고 리턴
    G[king_x] = king_y
    # 방문 처리
    visited.add((u,v))
    # union 성공
    return True

for tc in range(1, T+1):
    # V = 마지막 정점 번호
    # E = 간선의 개수
    V, E = map(int, input().split())

    graph = [] * E
    # 가중치로 정렬 해야한다. 정렬하기 편하려고
    for i in range(E):
        u, v, w = map(int, input().split())
        graph.append((w, u, v))
    # 방문 확인을 위한 세트
    visited = set()
    # 가중치 합산할 변수
    result = 0

    graph.sort(reverse=True)
    # make_set
    G = [i for i in range(V+1)]

    while graph:
        # 정렬된 리스트에서 제일 가중치가 작은 값 꺼내기
        w, u, v = graph.pop()
        # 방문한 적 있는지 확인
        if (u,v) in visited:
            continue
        # 유니온 가능한지 확인
        if union(u, v):
            # 가능하면 가중치 합산
            result += w

    print(f"#{tc} {result}")