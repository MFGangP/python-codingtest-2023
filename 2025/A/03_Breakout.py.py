from collections import deque
import sys
sys.stdin = open("Breakout_input.txt", "r")
sys.stdout = open("Breakout_output.txt", "w")

# 테스트 케이스 수
T = int(input())

def find_start_point(W : int, H : int, search_list : list):
   # WxH 횟수만큼 반복하면서 구슬 맞는 좌표 획득
    # 제일 상단에 있는 좌표만 맞출 수 있다.
    # 세로 기준으로 내려가면서 처음 나오는 값을 리스트에 추가
    for j in range(W):
        for i in range(H):
            # 좌표 값이 0이 아니라면 좌표 값 추가
            if array[i][j] >= 1:
                search_list.append([i, j])
                # 해당 열에서 첫 값 탐색이 끝났으니 다음 열 수색
                break

def break_block(roll_back: list, serach_queue: deque):
    cnt = 0
    while serach_queue:
        p, q = serach_queue.popleft()
        val = array[p][q]
        if val == 0: 
            continue
        roll_back.append([p, q, val])
        array[p][q] = 0
        cnt += 1
        for dp, dq in [[1,0], [-1,0], [0,-1], [0,1]]:
            for c in range(1, val):
                np, nq = p+dp*c, q+dq*c
                if 0 <= np < H and 0 <= nq < W and array[np][nq] > 0:
                    serach_queue.append([np, nq])
    return cnt

        
def reorder():
    # 전체 값이 합산 값 보다 작은 경우
    if total_value < sum_value:
        # 값 교체
        total_value = sum_value

for testcase in range(1, T + 1):
    # N = 구슬 쏘는 횟수
    # W = 가로 크기
    # H = 세로 크기
    N, W, H = map(int, input().split())

    array = [list(map(int, input().split())) for _ in range(H)]

    search_list = []
    serach_queue = deque()
    total_value = 0

    find_start_point(W, H, search_list)

    for i, j in search_list:
        serach_queue.append([i, j])
        roll_back = []
        sum_value = break_block(roll_back, serach_queue)

        if total_value < sum_value:
            total_value = sum_value

    print(f"#{testcase} {total_value}")