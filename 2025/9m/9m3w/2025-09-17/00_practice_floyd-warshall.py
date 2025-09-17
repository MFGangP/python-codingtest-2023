T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 인접행렬
    g = [list(map(int, input().split())) for _ in range(N)]

    # 플로이드워샬

    # 모든 노드 쌍 사이의 최단 거리 구하기
    # 음수 가중치 가능

    # 다익스트라
    # 정해진 시작노드에서 다른 노드까지의 최단거리 구하기
    # 음수 가중치 불가능

    # 거리 저장 배열
    # distances[i][j] == i번정점에서 j번정점까지의 최단거리
    # 처음에는 무한대로 설정
    distances = [[1e21 for _ in range(N)] for _ in range(N)]

    # 경유지가 없는 경우의 최단거리 초기화
    # 인접행렬을 참고해서 처음 최단거리 설정
    for i in range(N):
        for j in range(N):
            # i번 정점과 j번 정점 경유지가 없는경우 최단거리
            # 나중에 경유지를 추가하면서 최단거리 비교를통해 갱신
            if g[i][j] != 0:
                distances[i][j] = g[i][j]

    # 플로이드 워샬 알고리즘
    # 기존(i,j) 사이의 최단거리와 경유지 k정점을 거쳤을경우 최단거리 비교 => 더 작은 값 선택
    # distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])
    # DP 방식
    # 중간 경유지 정점번호 k의 범위를 점점 늘려가면서 비교
    # 경유지가 없는 경우 최단거리 distances 초기화

    # k = 0 : 경유지가 0번인경우

    # 경유지없는경우 vs 경유지가0번인경우 최단거리를 구하면된다.

    # k = 1 : 경유지가 1번인경우
    # 경유지없는경우,경유지가0번인경우 vs 경유지가1번인경우 최단거리를 구하면된다.

    # k = n-1 : 모든 가능한 경유지를 고려
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distances[i][j] = min(distances[i][k] + distances[k][j], distances[i][j])

    # 자기 자신까지의 거리는 0
    for i in range(N):
        distances[i][i] = 0

    # 시작이 i인 경우 최단거리의 최대값
    # 모든 i에 대해서 최대값 또 구하기
    max_v = max([max(i_lst) for i_lst in distances])

    print(f"#{tc} {max_v}")