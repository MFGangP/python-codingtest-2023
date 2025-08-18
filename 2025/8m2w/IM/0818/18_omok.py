import sys
sys.stdin = open("omok_input.txt", "r")
sys.stdout = open("omok_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    # N은 NxN 오목판 크기
    N = int(input())

    # NxN 배열
    array = [list(input()) for _ in range(N)]

    is_posible_omok = False

    for i in range(N):
        for j in range(N):
            if array[i][j] == "o":
                sum_omok = 1
            else:
                sum_omok = 0
            di = [-1, -1, 0, -1]
            dj = [0, -1, -1, 1]
            for x in range(4):
                for c in range(1, N):
                    ni, nj = i-di[x]*c, j-dj[x]*c
                    if 0<=ni<N and 0<=nj<N:
                        if array[ni][nj] == "o":
                            sum_omok += 1
                            if sum_omok >= 5:
                                is_posible_omok = True
                        else:
                            sum_omok = 0
                            
                    ni, nj = i+di[x]*c, j+dj[x]*c
                    if 0<=ni<N and 0<=nj<N:
                        if array[ni][nj] == "o":
                            sum_omok += 1
                            if sum_omok >= 5:
                                is_posible_omok = True
                        else:
                            sum_omok = 0

    print(f"#{testcase} ", end="")
    print("YES" if is_posible_omok else "NO")