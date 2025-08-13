import sys
sys.stdin = open("graph_root_input.txt", mode='r')
sys.stdout = open("graph_root_output.txt", mode='w') 

def find_path(graph, S, G, visited):
    # 스택에 S를 넣고 탐색 시작
    # 출발을 어디서부터 했는지 입력
    stack = [S]
    visited[S] = True    
    # 스택에 값이 있다면 계속 반복
    while stack:
        # 현재 노드는 스택에 있는 마지막 값 꺼내서 확인
        current_node = stack.pop()
        # 만약 현재 노드가 도착 노드이면
        if current_node == G:
            return 1
        # 현재 노드랑 인접해있는 이웃 노드 수만큼 반복
        for neighbor in graph[current_node]:
            # 인접 노드에 방문한 적이 없다면.
            if not visited[neighbor]:
                # 인접 노드 방문 기록 True
                visited[neighbor] = True
                # 스택에 인접 노드 등록 - 노드로 이동했다는 뜻
                stack.append(neighbor)

    return 0 # 종점 노드에 도착하지 못했다면 0을 반환

T = int(input())

for testcase in range(1, T+1):
    # V = 노드 개수
    # E = 간선의 수
    V, E = list(map(int, input().split()))
    # 연결된 노드의 정보 - E개
    node_line_info = [list(map(int, input().split())) for _ in range(E)]
    # S = 출발 노드
    # G = 도착 노드
    S, G = list(map(int, input().split()))
    # 인접 리스트를 표현하기 위한 리스트 - 1번부터 V번 까지 저장하기 위해
    # graph에는 u 노드와 연결된 다른 노드의 정보가 들어감.
    graph = [[] for _ in range(V + 1)]
    # 연결 노드 정보 인접 리스트에 등록
    for u, v in node_line_info:
        graph[u].append(v) # u에서 v로 가는 간선만 추가

    # 방문 기록, 스택 초기화
    visited = [False] * (V + 1)
    # 인접 리스트와 시작 노드, 종료 노드, 방문 정보
    result = find_path(graph, S, G, visited)

    print(f"#{testcase} {result}")