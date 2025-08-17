import sys
sys.stdin = open("ball_and_box_input.txt", mode='r')
sys.stdout = open("ball_and_box_output.txt", mode='w') 

T = int(input())

small = []
middle = []
big = []

for testcase in range(1, T+1):
    # 당근 개수
    N = int(input())
    # N개의 당근 크기 리스트
    Ci = list(map(int, input().split()))

    # 첫번째 박스의 범위 0~i
    for i in range(N):
        # 두번째 박스의 범위 i+1~j
        for j in range(i+1, N-i+1):
            # 세번째 박스의 범위 j+1~N-1
            pass   
        pass
    pass