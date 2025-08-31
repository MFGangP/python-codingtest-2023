from collections import deque
import sys
sys.stdin = open("Breakout_input.txt", "r")
sys.stdout = open("Breakout_output.txt", "w")

# 테스트 케이스 수
T = int(input())

def find_start_point(W, H):
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
    return 

def break_block():

    return 

for testcase in range(1, T + 1):
    # N = 구슬 쏘는 횟수
    # W = 가로 크기
    # H = 세로 크기
    N, W, H = map(int, input().split())

    array = [list(map(int, input().split())) for _ in range(H)]

    search_list = []
    serach_queue = deque()
    total_value = 0

 
    
    for i, j in search_list:
        sum_value = 1
        serach_queue.append([i, j])
        visited = [[0] * W for _ in range(H)]
        # 큐 내부가 비어있지 않으면 계속 반복
        while serach_queue:
            p, q = serach_queue.popleft()
            # 방문 한적 있는지 체크
            if visited[p][q] == 0:
                visited[p][q] = 1
            for dp, dq in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                # 현재 좌표 다음 값부터 시작
                for c in range(1, array[p][q]+1):
                    np, nq = p+dp*c, q+dq*c
                    # ni,nj가 범위 안이고 방문한적이 없는 노드라면
                    if 0 <= np < H and 0 <= nq < W and visited[np][nq] == 0:
                        # 방문 기록 변경
                        visited[np][nq] = 1
                        # array[ni][nj]가 1보다 크다면
                        if array[np][nq] > 1:
                            # deque에 탐색해야하는 좌표(2이상의 값을 가진 좌표 값) 추가
                            serach_queue.append([np, nq])
                            sum_value += 1
        # 전체 값이 합산 값 보다 작은 경우
        if total_value < sum_value:
            # 값 교체
            total_value = sum_value
    print(f"#{testcase} {total_value}")