from collections import deque
import sys
sys.stdin = open("Breakout_input.txt", "r")
sys.stdout = open("Breakout_output.txt", "w")

# 테스트 케이스 수
T = int(input())

for testcase in range(1, T + 1):
    # N = 구슬 쏘는 횟수
    # W = 가로 크기
    # H = 세로 크기
    N, W, H = map(int, input().split())

    array = [list(map(int, input().split())) for _ in range(H)]

    search_list = []
    serach_queue = deque()
    total_value = 0

    # WxH 횟수만큼 반복하면서 구슬 맞는 좌표 획득
    # 제일 상단에 있는 좌표만 맞출 수 있다.
    # 세로 기준으로 내려가면서 처음 나오는 값을 리스트에 추가
    for i in range(W):
            for j in range(H):
                # 좌표 값이 0이 아니라면 좌표 값 추가
                if array[i][j] >= 1:
                    search_list.append([j, i])
                    # 해당 열에서 첫 값 탐색이 끝났으니 다음 열 수색
                    break

    for i, j in search_list:
        serach_queue.append([i, j])
        p, q = serach_queue.popleft()
        sum_value = array[q][p]
        for di, dj in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
            # 시작 지점 값 sum_value에 추가
            for c in range(array[q][p]):
                ni, nj = i+di*c, j+dj*c
                # ni,nj가 범위 안이라면
                if 0 <= ni < H and 0 <= nj < W:
                    sum_value += array[ni][nj]
                    # array[ni][nj]가 1보다 크다면
                    if array[ni][nj] > 1:
                        # deque에 탐색해야하는 좌표(2이상의 값을 가진 좌표 값) 추가
                        serach_queue.append([p, q])

        # 전체 값이 합산 값 보다 작은 경우
        if total_value < sum_value:
            # 값 교체
            total_value = sum_value
            