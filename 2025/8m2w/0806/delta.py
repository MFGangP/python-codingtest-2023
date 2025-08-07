max_v = 0

arr = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
N=4
k=2

for i in range(N):
    for j in range(N):
        # i, j를 중심으로 중심점 S
        # 여기가 시작되는 기준
        s = arr[i][j]
        # 이 밑으로 어떤 값을 수집할건지 정한다.

        # 접근하고 싶은 순서대로
        # 각 방향 상,하,좌,우 
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]: 
            # 거리별 기준점에서 어디까지 갈 껀지 곱해주는 값 c
            for c in range(1, k+1): 
                ni, nj = i+di*c, j+dj*c
                # 범위 밖으로 나갔는지 아닌지 확인하는 구문
                # N의 값이 4면 0~3안인지 
                # 여기서 특정 조건을 줘서 떨어트릴 값을 정한다.
                if 0<=ni<N and 0<=nj<N: 
                    s += arr[ni][nj]
        if max_v < s:
            max_v = s
    print(max_v)