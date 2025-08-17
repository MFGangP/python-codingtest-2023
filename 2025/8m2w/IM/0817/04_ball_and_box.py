import sys
sys.stdin = open("ball_and_box_input.txt", mode='r')
sys.stdout = open("ball_and_box_output.txt", mode='w') 

T = int(input())

for testcase in range(1, T+1):
    B, W, X, Y, Z = map(int, input().split())
    
    # 1. 같은 색깔로 짝짓는 것을 기본으로 점수 계산
    score = (B * X) + (W * Y)
    # 2. 서로 다른 색깔로 바꿔 넣었을 때의 이득 계산
    profit = (2 * Z) - (X + Y)
    
    # 3. 만약 바꿔 넣는 것이 이득이라면
    if profit > 0:
        # 4. 바꿀 수 있는 쌍의 최대 개수는 B와 W 중 더 작은 값
        num_swaps = min(B, W)
        # 5. 최대 점수 = 기본 점수 + (이득 * 바꿀 수 있는 횟수)
        score += num_swaps * profit
    
    print(f"#{testcase} {score}")