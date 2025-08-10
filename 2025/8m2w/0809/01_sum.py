import sys

sys.stdin = open("sum_input.txt", mode='r')
sys.stdout = open("sum_output.txt", mode='w')


for _ in range(10):
    N = 100
    time = int(input())
    Array = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0

    for i in range(N):
        sum_value = 0
        for j in range(N):
            sum_value += Array[i][j]
        # 행 별로 반복할 때 값 변경
        if max_value < sum_value:
            max_value = sum_value

    for i in range(N):
        sum_value = 0
        for j in range(N):
            sum_value += Array[j][i]
        # 열 별로 반복할 때 값 변경
        if max_value < sum_value:
            max_value = sum_value

    for i in range(N):
        sum_value = Array[i][i]
        # 우하향으로 반복할 때 값 변경
        if max_value < sum_value:
            max_value = sum_value

    for i in range(N):
        sum_value = Array[N-i-1][N-i-1]
        # 좌상향으로 반복할 때 값 변경
        if max_value < sum_value:
            max_value = sum_value

    print(f"{time} {max_value}")