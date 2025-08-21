import sys
sys.stdin = open("ancient_ruins_input.txt", mode='r')
sys.stdout = open("ancient_ruins_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    N, M = map(int, input().split())

    # NxM 배열 선언
    array = [list(map(int, input().split())) for _ in range(N)]
    max_len = 0

    for i in range(N):
        for j in range(M):
            count = 0
            # 만약 행 체크 중 값이 1이면
            if array[i][j] == 1:
                x = j + 1
                count += 1
                # 좌표가 1이면 계속
                while 0<=x<M and array[i][x] == 1:
                    x += 1
                    count += 1
                if count >= 2 and max_len < count:
                    max_len = count
            else: 
                count = 0
    for j in range(M):
        for i in range(N):
            count = 0
            # 만약 행 체크 중 값이 1이면
            if array[i][j] == 1:
                x = i + 1
                count += 1
                # 좌표가 1이면 계속
                while 0<=x<N and array[x][j] == 1:
                    x += 1
                    count += 1
                if count >= 2 and max_len < count:
                    max_len = count
            else: 
                count = 0
    print(f"#{testcase} {max_len}")