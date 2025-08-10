import sys

sys.stdin = open("snail_num_input.txt", mode='r')
sys.stdout = open("snail_num_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):

    N = int(input())

    array = [[0] * N for _ in range(N)]

    snail_num = 1
    i, j = 0, 0

    di = [0, 1, 0, -1] 
    dj = [1, 0, -1, 0]
    direction = 0

    # 몇 번 돌아야할 지 모르니까 while
    while(snail_num <= N*N):
        # 서있는 곳에 값 대입
        array[i][j] = snail_num
        # 값 넣어줬으니까 +1
        snail_num += 1

        # 다음 좌표가 어디인지 1차 계산
        ni = i + di[direction]
        nj = j + dj[direction]
        # 만약 다음 좌표에 값이 0이거나 범위를 초과했을 경우 재 계산
        if not (0<=ni<N and 0<=nj<N and array[ni][nj] == 0):
            # 1 더한 다음 나머지 값을 재 대입
            direction = (direction + 1) % 4
            # 다음 좌표가 어디인지 2차 계산
            ni = i + di[direction]
            nj = j + dj[direction]
        # 위치 업데이트
        i, j = ni, nj

    print(f"#{time}")
    for idx in range(N):
        print(*array[idx])