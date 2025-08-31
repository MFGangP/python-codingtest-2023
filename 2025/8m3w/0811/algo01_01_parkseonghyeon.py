# 배열 크기 M*M

# K개의 별을 포함하는 영역찾기
# 조건 만족하는 영역은 하나 이하 0~1

# *의 갯수 찾는게 목적

# 테스트 케이스 개수
T = int(input())

for time in range(1, T+1):
    # N은 전체 배열 크기
    # M은 찾아야할 배열 크기
    # K는 별의 개수
    N, M, K = list(map(int, input().split()))
    # 배열 입력 받기
    array = [list(map(str, input())) for _ in range(N)]

    # 최고 갯수 좌표
    x, y = 0, 0
    # 정확하게 일치하는 배열의 수
    correct_area = 0

    # 전체 배열 크기
    # 내가 탐색할 배열의 크기를 뺀 크기로 재 배당
    for i in range(N-M+1):
        for j in range(N-M+1):
            # * 개수의 합 변수
            sum_vaule = 0
            for p in range(M):
                for g in range(M):
                    # p,g 만큼 더한 좌표 값이 *이면
                    if array[i+p][j+g] == "*":
                        sum_vaule += 1
            # 정확히 K 개의 갯수를 가진 영역일때만
            if sum_vaule == K:
                # 정확히 일치하는 구역 값 += 1 해주고
                correct_area += 1
                # 좌표 값을 갱신
                x = i
                y = j
            # 다 돌았는데도 correct_area가 없으면
            elif correct_area <= 0:
                x = y = -1

    print(f"#{time} {x} {y}")
