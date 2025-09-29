T = int(input())

for tc in range(1, T+1):
    # N = 계산할 원본 2차원 배열 크기
    # M = 계산 식을 담고 있는 2차원 배열 크기
    N, M = map(int, input().split())
    # 계산할 대상을 담고 있는 배열
    matrix = [list(map(int, input().split())) for _ in range(N)]
    # 계산식을 담고 있는 2차원 배열
    score = [list(map(int, input().split())) for _ in range(M)]
    # 계산한 값을 넣을 2차원 배열
    results = [[0] * (N-M+1) for _ in range(N-M+1)]

    # 크기 초과되지 않는 범위의 배열 탐색
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 계산식 크기만큼 순회
            for p in range(M):
                for q in range(M):
                    # M칸 만큼 진행하면서 값 계산하여 더해주기
                    results[i][j] += matrix[i+p][j+q] * score[p][q]

    print(f"#{tc}")
    for k in range(N-M+1):
        for l in range(N-M+1):
            # 출력 형식 맞추기
            if l != (N-M):
                print(results[k][l], end=" ")
            else:
                print(results[k][l])