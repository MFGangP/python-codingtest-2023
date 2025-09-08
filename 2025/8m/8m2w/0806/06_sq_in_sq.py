T = int(input())

for time in range(1, T+1):
    # N : 큰 정사각형의 크기
    # M : 내부에 있는 작은 정사각형의 크기
    N, M = map(int, input().split())

    # N*N 2차원 배열 만들기
    matrix = [[0] * N for _ in range(N)]

    # 큰 정사각형 내부에 적을 작은 정사각의 번호
    square = 1

    # 큰 정사각형의 모든 위치에서 작은 정사각형 만들기 시작
    # 작은 정사각형을 만들기 시작할 수 있는 위치를 예상 가능
    # 큰 정사각형의 마지막 인덱스 N-1
    # (N-1, N-1)에서 작은 정 사각형을 만들기 시작하면
    # 작은 정사각형은 (N, N) 이런 위치를 포함하게 된다.
    # 큰 사각형에서는 이 위치가 접근 불가능한 인덱스(범위를 벗어남)

    # 미리 시작 위치를 작은 정사각형의 크기 만큼 뺀 상태에서 순회
    for i in range(N-M+1):
        for j in range(N-M+1):
            # 작은 정사각형을 만들기 시작하는 위치 (i,j)
            # (i+0,j) (i+0,j+1) ... (i+0, j+M-1)
            # (i+1,j) (i+1, j+1) .... (i+1, j+M-1)
            # ...
            # (i+M-1, j) (i+M-1, j+1) ... (i+M-1, j+M-1)
            
            # 작은 정사각형의 행 번호 si, 열 변호 sj
            for si in range(i, i+M):
                for sj in range(j, j+M):
                    if 0 <= si < N and 0 <= sj < N:
                       matrix[si][sj] = square

            # 작은 정사각형을 한번 다 표시했으면 숫자 + 1
            square += 1

    print(f"#{time}")
    for i in range(N):
        print(*matrix[i])