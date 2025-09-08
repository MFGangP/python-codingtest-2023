T = int(input())

for time in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [[0] * N for _ in range(N)]
    max_sum = 0
    for i in range(N):
        matrix[i] = list(map(int, input().split()))
    for i in range(N-(M-1)):
        for j in range(N-(M-1)):
            # 배열 총 갯수 만큼 반복해야하기 때문
            sum_value = 0
            for x in range(M):
                for y in range(M):
                    sum_value += matrix[i+x][j+y]
            if max_sum < sum_value:
                max_sum = sum_value
    print(f"#{time} {max_sum}")