# 테스트 케이스
T = int(input())

for time in range(1, T+1):
    # N은 열의 개수
    # M은 행의 개수
    N, M = list(map(int, input().split()))

    array = [list(map(int, input().split())) for _ in range(N)]
    # 각 구역의 높이 Hji 0 이상 20 이하
    num_of_safe_area = 0

    # 지도 가장자리 구역은 제외 1부터 N-1, M-1까지
    for i in range(1, N-1):
        for j in range(1, M-1):
            hji = 0
            # 좌상 -> 상 -> 우상 -> 우 -> 우하 -> 하 -> 좌하 -> 좌
            for di, dj in [[-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1], [0,-1]]:
                ni, nj = i+di, j+dj
                # 비교할 값이 기준보다 낮거나 같다면
                if array[ni][nj] <= array[i][j]:
                    # 안전구역 개수 += 1
                    hji += 1
            # 만약 모든 사방이 나보다 낮은 값이라면
            if hji >= 8:
                num_of_safe_area += 1
    print(f"#{time} {num_of_safe_area}")