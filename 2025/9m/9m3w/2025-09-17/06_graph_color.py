import sys
sys.stdin = open("graph_color_input.txt", "r")

def is_checked(node, c):
    for neighbor in g[node]:
        # 만약 이웃 노드가 이미 c와 같은 색으로 칠해져 있다면
        if color[neighbor] == c:
            return False # 이 색은 칠할 수 없음
        
    # 모든 이웃을 확인했는데 같은 색이 없으면
    return True

def solve(node_idx):
    # 종료 조건
    # 모든 노드(N번)를 다 칠하고 그 다음 노드로 넘어왔다면
    if node_idx == N + 1:
        return True

    # 재귀 단계
    # 현재 노드(node_idx)에 1번부터 M번까지의 모든 색을 칠해본다.
    for c in range(1, M + 1):
        # 만약 c 색깔을 칠하는 것이 가능하면
        if is_checked(node_idx, c):
            color[node_idx] = c # c 색깔로 칠한다.
            
            # 다음 노드를 칠하러 재귀 호출을 하고, 그 결과가 성공이라면
            if solve(node_idx + 1):
                return True # 성공을 반환하며 종료
    
    # 1번부터 M번까지 모든 색을 시도해봤는데 실패했다면
    return False

T = int(input())
for tc in range(1, T + 1):
    N, E, M = map(int, input().split())
    
    # 인접 리스트
    g = [[] for _ in range(N + 1)] 
    for _ in range(E):
        s, e = map(int, input().split())
        g[s].append(e)
        g[e].append(s)

    # 각 노드의 색깔 정보를 저장할 배열 0: 색칠 안됨
    color = [0] * (N + 1)

    # 1번 노드부터 색칠 시작
    if solve(1):
        result = 1 # 성공
    else:
        result = 0 # 실패

    print(f"#{tc} {result}")