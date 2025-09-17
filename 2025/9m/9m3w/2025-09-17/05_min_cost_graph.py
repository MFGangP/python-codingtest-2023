# 유향 그래프에 대해 인접 노드로 이동하는 비용을 기록한 인접 행렬
# 최소 이동 비용 - 다익스트라 인데 얘는 음수가 있다.
# 플로이드 워셜 - 음수 가능
import sys
sys.stdin = open("min_cost_graph_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    g = [list(map(int, input().split())) for _ in range(N)]

    distances = [[float("inf") for _ in range(N)] for _ in range(N)]
    # i에서 j로 갈 때의 가중치
    for i in range(N):
        for j in range(N):
            if g[i][j] != 0:
                 distances[i][j] = g[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

    for i in range(N):
        distances[i][i] = 0

    max_v = max([max(i_lst) for i_lst in distances])

    print(f"#{tc} {max_v}")