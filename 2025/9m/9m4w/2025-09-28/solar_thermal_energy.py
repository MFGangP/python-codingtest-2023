import sys
sys.stdin = open("solar_thermal_energy_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    L = N-M+1
    matrix = [list(map(int, input().split())) for _ in range(N)]
    score = [list(map(int, input().split())) for _ in range(M)]
    result = [[0] * (L)for _ in range(L)]

    for i in range(L):
        for j in range(L):
            for p in range(M):
                for q in range(M):
                    ni , nj = i+p, j+q
                    if 0 <= ni <= L and 0 <= ni <= L:
                        result[i][j] += matrix[ni][nj] + score[p][q]
    
    print(f"#{tc}")
    for n in range(L):
        for m in range(L):
            if m != L-1:
                print(result[n][m], end=" ")
            else:
                print(result[n][m])