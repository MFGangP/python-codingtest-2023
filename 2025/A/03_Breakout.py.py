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

    # W 횟수만큼 반복하면서 구슬 맞는 좌표 획득
    # 제일 상단에 있는 좌표만 맞출 수 있다.
    for i in range(W):
        pass