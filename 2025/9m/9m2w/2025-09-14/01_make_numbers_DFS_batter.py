import sys
sys.stdin = open("make_numbers_input.txt", "r")
sys.stdout = open("make_numbers_output.txt", "w")

def solve(index, current_value):
    """
    index: 다음에 사용할 숫자의 인덱스
    current_value: index-1까지 계산된 중간 결과
    """
    global min_result, max_result

    # 종료 조건: 모든 숫자를 다 사용했다면
    if index == N:
        min_result = min(min_result, current_value)
        max_result = max(max_result, current_value)
        return

    # 재귀 호출: 사용 가능한 연산자를 하나씩 적용해봄
    # 덧셈(+)
    if op_counts[0] > 0:
        op_counts[0] -= 1 # '+' 연산자 하나 사용
        solve(index + 1, current_value + numbers[index])
        op_counts[0] += 1 # 백트래킹: 사용했던 연산자 복구
    
    # 뺄셈(-)
    if op_counts[1] > 0:
        op_counts[1] -= 1
        solve(index + 1, current_value - numbers[index])
        op_counts[1] += 1
        
    # 곱셈(*)
    if op_counts[2] > 0:
        op_counts[2] -= 1
        solve(index + 1, current_value * numbers[index])
        op_counts[2] += 1
        
    # 나눗셈(/)
    if op_counts[3] > 0:
        op_counts[3] -= 1
        solve(index + 1, int(current_value / numbers[index]))
        op_counts[3] += 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # op_counts: [+, -, *, /] 순서대로 연산자 개수
    op_counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    min_result = float("inf")
    max_result = float("-inf")

    # 1번 인덱스 숫자부터, 초기값은 0번 인덱스 숫자로 시작
    solve(1, numbers[0])

    print(f"#{tc} {max_result - min_result}")