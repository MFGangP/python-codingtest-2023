import sys
sys.stdin = open("tree_height_input.txt", "r")
sys.stdout = open("tree_height_output.txt", "w")

# 테스트 케이스 수
T = int(input())

def solve():
    # 나무의 개수
    N = int(input())
    # 나무들의 높이
    Trees = list(map(int, input().split()))

    # 목표 높이
    target_height = max(Trees)

    # 1씩 자라게 하는 물 주기 횟수와 2씩 자라게 하는 물 주기 횟수
    total_ones = 0
    total_twos = 0
    
    # 각 나무에 대해 필요한 물 주기 횟수 계산
    for i in range(N):
        growth_needed = target_height - Trees[i]
        total_ones += growth_needed % 2
        total_twos += growth_needed // 2

    # 최소 날짜 계산
    days = 0
    if total_twos > total_ones:
        # 2씩 자라는 물 주기가 더 많을 경우
        # 1-2-1-2... 패턴으로 성장
        # total_ones 만큼 1씩 주고, total_ones 만큼 2씩 줌
        days += total_ones * 2
        
        # 남은 2 성장 물 주기 횟수
        remaining_twos = total_twos - total_ones
        
        # 남은 2성장 물 주기 횟수를 3(1+2)으로 묶어 날짜 계산
        days += (remaining_twos // 3) * 2
        if remaining_twos % 3 == 1:
            days += 1
        elif remaining_twos % 3 == 2:
            days += 2
            
    elif total_twos <= total_ones:
        # 1씩 자라는 물 주기가 더 많거나 같을 경우
        # 2-1-2-1... 패턴으로 성장
        # total_twos 만큼 2씩 주고, total_twos 만큼 1씩 줌
        days += total_twos * 2
        
        # 남은 1 성장 물 주기 횟수
        remaining_ones = total_ones - total_twos
        
        # 남은 1 성장 물 주기 횟수를 2(1+1)로 묶어 날짜 계산
        days += remaining_ones + (remaining_ones // 2)

    return days

for testcase in range(1, T + 1):
    result = solve()
    print(f"#{testcase} {result}")