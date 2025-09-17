import sys
sys.stdin = open("swimming_pool_input.txt", "r")
sys.stdout = open("swimming_pool_output.txt", "w")

T = int(input())
for tc in range(1, T + 1):
    day_cost, months_cost, months_3_cost, year_cost = map(int, input().split())
    months = list(map(int, input().split()))
    
    # DP 테이블 초기화 (1월부터 12월까지 사용하기 위해 13칸)
    dp = [0] * 13

    # 1월부터 12월까지 순차적으로 계산
    for i in range(1, 13):
        # 현재 월의 인덱스는 i, plan 리스트의 인덱스는 i-1
        
        # 선택 1: 이번 달을 [1일권] 또는 [1달권]으로 해결하는 경우
        # (i-1)월까지의 최소 비용 + 이번 달 비용
        cost_this_month = dp[i-1] + min(months[i-1] * day_cost, months_cost)
        
        # 기본적으로 이번 달 최소 비용은 위 계산값으로 설정
        dp[i] = cost_this_month

        # 선택 2: 이번 달을 [3달 이용권]의 마지막 달로 보고 해결하는 경우
        # (3월 이상부터만 가능)
        if i >= 3:
            # (i-3)월까지의 최소 비용 + 3달 이용권 가격
            cost_with_3month_pass = dp[i-3] + months_3_cost
            dp[i] = min(dp[i], cost_with_3month_pass)
            
    # 최종적으로, 12개월 DP 계산 결과와 1년 이용권 가격을 비교
    min_total_cost = min(dp[12], year_cost)
    
    print(f"#{tc} {min_total_cost}")