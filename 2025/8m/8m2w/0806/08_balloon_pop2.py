import sys
sys.stdin = open("balloon_input2.txt", mode='r')
sys.stdout = open("balloon_output2.txt", mode='w')

T = int(input())


for time in range(1, T+1):
    N, M = list(map(int, input().split()))

    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_sum = 0 

    for i in range(N):
        for j in range(M):
            point_sum = matrix[i][j]
            for di, dj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M:
                    point_sum += matrix[ni][nj]
            if max_sum < point_sum:
                max_sum = point_sum
    print(f"#{time} {max_sum}")    