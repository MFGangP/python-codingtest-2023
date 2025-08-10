import sys

sys.stdin = open("snail_num_input.txt", mode='r')
sys.stdout = open("snail_num_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):

    N = int(input())

    array = [[0] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1], [1,0], [0,-1], [-1,0]]:
                for c in range(1, N+1):
                    ni, nj = i+di*c, j+dj*c
                    if 0<=ni<N and 0<=nj<N:
                        array[ni][nj] += 1

    print(f"#{time}")
    for i in range(len(array)):
        print(*array[i])