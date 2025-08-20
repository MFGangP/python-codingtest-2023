import sys
sys.stdin = open("arm_wrestling_input.txt", "r")
sys.stdout = open("arm_wrestling_output.txt", "w")

T = int(input())
# 팔씨름 15번 중 8번 이상 이기는 사람이 점심 값 면제.
for testcase in range(1, T+1):
    # S[i]가 o면 소정이 가 i번째 경기에서 승리, x면 i 번째 경기에서 패배
    S = list(input())
    
    win_num = 0
    lose_num = 0

    for result in S:
        if result == "o":
            win_num += 1
            
    # 소정이가 점심값을 면제받을 가능성이 있으면 Yes 없으면 NO
    if (15 - len(S) + win_num >= 8):
        print(f"#{testcase} YES")
    else:
        print(f"#{testcase} NO")

