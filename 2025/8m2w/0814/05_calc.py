import sys
sys.stdin = open("calc_input.txt", mode='r')
sys.stdout = open("calc_output.txt", mode='w') 

# 스택 밖에 있을때 우선순위
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
# 스택 안에 있을때 우선순위
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}

def postfix(texts):
    postfix = ""
    stack = []

    for token in texts:
        # 토큰이 비연산자 라면
        if token not in "()+-*/":
            # 스택에 연산자 추가
            postfix += token
        # 토큰이 연산자 라면 
        else:
            # 토큰이 ) 라면
            if token == ")":
                # 스택에서 모든 숫자 꺼내서 식 만들기
                while stack:
                    # 꺼낸 오퍼레이터가
                    operator = stack.pop()
                    # (여는 괄호라면 종료
                    if operator == "(":
                        break
                    # 나머지라면 
                    else:
                        # 오퍼레이터 추가
                        postfix += operator
            # 토큰이 닫는 괄호가 아닌 다른 연산자였다면
            else:
                # 스택안에 현재 token 보다 우선순위가 같거나 높은 연산자는 다 꺼내쓴다
                while stack and icp[token] <= isp[stack[-1]]:
                    # 꺼내서 결과에 이어붙이기
                    postfix += stack.pop()

                # token의 우선순위가 스택의 꼭대기에 있는 연산자의 우선순위보다 높았다면
                # 또는 스택이 비어있다면
                stack.append(token)
    
    # 모든 토큰을 확인 한 후에 스택에 남아있는 연산자는 그대로 차례대로 출력
    while stack:
        postfix += stack.pop()

    return postfix

def prefix(postfix):
    stack = []
    
    for token in postfix:
        # postfix 에서 나온 값이 숫자라면
        if token not in "()+-*/":
            stack += token
        # postfix 에서 나온 값이 연산자라면
        else:
            if token == "*":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a*b)
            elif token == "/":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a/b)
            elif token == "+":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif token == "-":
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
    # for 문이 정상적으로 종료 되었다면
    else:
        # 스택 내부에 남은 값이 하나라면
        if len(stack) == 1:
            return stack.pop() 

for testcase in range(1, 11):
    # 테스트 케이스 길이
    texts_len = int(input())

    #테스트 케이스
    texts = input()

    result = postfix(texts)
    result = prefix(result)

    print(f"#{testcase} {result}")

    # print(result)