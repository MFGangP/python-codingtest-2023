import sys
sys.stdin = open("graph_input.txt", "r")
sys.stdout = open("graph_output.txt", "w")

T = int(input())

def find_path(graph, S, G, visited):
    #스택에 시작점 S 넣고 시작
    stack = [S]
    # 방문 기록에 True
    visited[S] = True

    # 스택이 차있는 동안.
    while stack:
        # 스택에 있는 마지막 값 꺼내서 확인
        current_node = stack.pop()
        # 현재 노드가 도착지라면
        if current_node == G:
            return 1
    
        # 현재 노드랑 인접해있는 노드 방문
        for neighber in graph[current_node]:
            # 이웃 노드에 방문한 적이 없다면.
            if not visited[neighber]:
                # 방문 기록 True
                visited[neighber] = True
                # 스택에 노드 등록 = 이동했다는 뜻.
                stack.append(neighber)
    # 다 돌아도 없으면 실패 했다는 뜻
    return 0

for testcase in range(1, T+1):
    # V = 노드 개수
    # E = 간선의 수
    V, E = list(map(int, input().split()))
    # 연결된 노드의 정보 - E개
    node_line_info = [list(map(int, input().split())) for _ in range(E)]
    # S = 출발 노드
    # G = 도착 노드
    S, G = list(map(int, input().split()))

    # 그래프 리스트 - 노드 정보를 담기위한 리스트 V개
    graph = [[] for _ in range(V+1)]

    # 그래프 리스트에 노드 연결 기입.
    for u, v in node_line_info:
        graph[u].append(v)
    # 방문 기록, 스택 초기화
    visited = [False] * (V+1)

    # 인접 리스트, 시작점, 종료노드, 방문기록
    result = find_path(graph, S, G, visited)
    
    print(f"#{testcase} {result}")

