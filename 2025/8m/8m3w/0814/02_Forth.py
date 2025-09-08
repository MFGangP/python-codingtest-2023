# import sys
# sys.stdin = open("forth_input.txt", mode='r')
# sys.stdout = open("forth_output.txt", mode='w') 

def prefix(texts):
    # 피연산자를 넣은 스텍
    stack = []

    for token in texts:
        # 피연산자라면
        if token.isdigit():
            # 스텍에 넣기
            stack.append(int(token))
        # 연산자라면
        elif token in "+-*/":
            if len(stack) >= 2:
                b = stack.pop()
                a = stack.pop()
            else:
                return "error"
            
            if token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b)
            elif token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
        # . 이라면
        elif token == ".":
            # stack에 값이 1개만 남았다면 최종 값        
            if len(stack) == 1:
                # 최종값 리턴
                return stack.pop()
            # 1개가 아니라면 에러
            else:
                return "error"
    # 정상적으로 값을 만나지 못했다면
    return "error"

T = int(input())

for testcase in range(1, T+1):
    texts = input().split()

    result = prefix(texts)

    print(f"#{testcase} {result}")
