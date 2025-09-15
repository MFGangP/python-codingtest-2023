T = int(input())

def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
# 인덱스, 타켓 리스트, 방문 기록
def dfs(idx, target_list, visited):
    global min_value
    # 탈출 조건
    if idx == N:
        result = 0
        # 마지막에 되돌아와야하기 때문에 추가
        target_list.append([0, 0])
        # 모든 요소에 다 방문했다면 시작점 부터 끝지점 까지
        for p in range(len(target_list)-1):
            i, j = target_list[p]
            x, y = target_list[p+1]
            result += calc_distance(i, j, x, y)
        min_value = min(min_value, result)
        # 계산 끝났으면 되돌아 가기전에 pop()
        target_list.pop()
        return

    for i in range(len(target)):
        # 해당 타겟에 방문한 적이 없다면
        if not visited[i]:
            # 재귀 진입
            visited[i] = True # 방문 처리
            target_list.append((target[i]))
            dfs(idx + 1, target_list, visited)
            target_list.pop() # 백트래킹
            visited[i] = False

for tc in range(1, T+1):
    N = int(input())
    min_value = float("inf")
    target = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N

    for i in range(N):
        dfs(0, [[0,0]], visited)

    print(f"#{tc} {min_value}")