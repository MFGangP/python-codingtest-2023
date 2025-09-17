import sys
sys.stdin = open("make_numbers_input.txt", "r")
sys.stdout = open("make_numbers_output.txt", "w")

def solve(index):
    global min_result, max_result
    # 탈출 조건 : 연산자 횟수 만큼 돌았으면 종료
    if index == N - 1:
        result = numbers[0]
        
        for i in range(N - 1):
            op = current_operator[i]
            num = numbers[i+1]
            
            if op == "+": 
                result += num
            elif op == "-": 
                result -= num
            elif op == "*": 
                result *= num
            elif op == "/":
                result = int(result / num)
        
        # 최대, 최소값 갱신
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return
    
    # 재귀 호출
    for i in range(N - 1):
        if not visited[i]:
            visited[i] = True
            current_operator.append(operators[i])
            solve(index + 1)
            current_operator.pop()
            visited[i] = False

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    op_counts = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    operators = []
    operator_symbols = ["+", "-", "*", "/"]
    for i in range(4):
        operators.extend([operator_symbols[i]] * op_counts[i])
    
    visited = [False] * (N - 1)
    current_operator = []
    min_result = float("inf")
    max_result = float("-inf")

    solve(0)

    print(f"#{tc} {max_result - min_result}")