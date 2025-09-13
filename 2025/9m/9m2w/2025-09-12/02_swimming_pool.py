import sys

sys.stdin = open("swimming_pool_input.txt", "r")
sys.stdout = open("swimming_pool_output.txt", "w")

T = int(input())

# 종료 조건 : 12월을 모두 고려한 경우
# 가지의 수 : 4개 (1일, 1달, 3달, 1년)
def solve(month, total_cost):
    # 12달을 다 계산했으니 최소값 계산
    global min_answer
    # 탈출 조건
    if month > 12:
        # Todo : 최소값 갱신
        min_answer = min(min_answer, total_cost)
        return 
    
    # 가지의 수
    # 1일권으로 다 사는 경우
    solve(month+1, total_cost + (days[month] * cost_day))
    # 1달권으로 다 사는 경우
    solve(month+1, total_cost + cost_month)
    # 3달권으로 다 사는 경우
    solve(month+3, total_cost + cost_month_3)
    # 1년 이용권으로 사는 경우
    solve(month+12, total_cost + cost_year)

for tc in range(1, T+1):
    # 이용권 가격들 (1일, 1달, 3달, 1년)
    cost_day, cost_month, cost_month_3, cost_year = map(int, input().split())
    # 인덱스 계산하기 귀찮으니까 0을 더해서 만든다.
    # 12개월 이용 계획 (1부터 쓴다)
    days = [0] + list(map(int, input().split()))

    min_answer = 31 * 12 * 3000 # 최대 금액 (31일 * 12개월 * 3000)
    
    # 1월부터 시
    solve(1, 0)

    print(f"#{tc} {min_answer}")