import sys
sys.stdin = open("find_root_input.txt", mode='r')
sys.stdout = open("find_root_output.txt", mode='w') 

# 초기화된 vertex_list에 노드 연결 정보 등록
def insert_node_in_vertex_list(nodes, vertex1, vertex2):
    # 받은 노드 정보로 98번째 노드까지
    # 노드 개수가 최대 2개를 넘기지 않기 때문에 번갈아가면서 저장
    # 순서 쌍으로 주어지기 때문에 2개마다 값 체크
    for i in range(0, len(nodes), 2):
        # 첫 번째 정점이 빈값이라면
        if vertex1[nodes[i]] == None:
            # 다음 노드 정보를 등록
            vertex1[nodes[i]] = nodes[i+1]
        # 첫번째 정점에 이미 노드가 연결되어 있다면
        else:
            vertex2[nodes[i]] = nodes[i+1]

    return vertex1, vertex2

def search_root(vertex1, vertex2, S, G, visited):
    # 출발지는 0으로 고정이기 때문에 스택에 등록
    stack = [S]
    visited[S] = True
    # 스택이 비어있지 않으면 계속해서 반복
    while stack:
        # 현재 노드는 스택에서 꺼내서 확인
        current_node = stack.pop()

        # 현재 노드가 도착 지점이라면
        if current_node == G:
            return 1

        # vertex에 현재 노드 값이 빈값이 아니고 방문한적이 없는 노드라면 방문        
        # vertex1에 연결된 노드가 있다면
        if vertex1[current_node] is not None and not visited[vertex1[current_node]]:
            visited[vertex1[current_node]] = True
            stack.append(vertex1[current_node])

        # vertex2에 연결된 노드가 있다면
        if vertex2[current_node] is not None and not visited[vertex2[current_node]]:
            visited[vertex2[current_node]] = True
            stack.append(vertex2[current_node])

    # 연결된 노드가 없을 때
    return 0


# 테스트 케이스는 10개
for _ in range(1, 11):
    # 테스트 케이스 번호, 길의 총 개수
    testcase, road_numbers = list(map(int, input().split()))
    # 노드 정보
    nodes = list(map(int, input().split()))
    # 출발점, 도착점
    S = 0
    G = 99
    # 노드 연결 상태를 표시하기 위한 리스트
    # 최대 노드 연결 2개 이기 때문에 중복 걱정 X
    vertex1 = [None for _ in range(100)]
    vertex2 = [None for _ in range(100)]
    # 방문 했는지 기록 하기위한 Bool 타입 리스트
    visited = [False for _ in range(100)]
    # vertex 정보 갱신
    vertex1, vertex2 = insert_node_in_vertex_list(nodes, vertex1, vertex2)
    # 시작 지점부터 종료 지점 까지 연결되어있는지 확인
    result = search_root(vertex1, vertex2, S, G, visited)

    print(f'#{testcase} {result}')