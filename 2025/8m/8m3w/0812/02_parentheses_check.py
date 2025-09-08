def check_parentheses(text, stack):
    top = -1
    # 받은 텍스트 내부 값으로 반복
    for x in text:
        # 내부 값이 여는 괄호 일 때
        if x in ['(','{']: # ,'['
            # top 개수 += 1
            top += 1
            # stack에 추가
            stack[top] = x
        # 내부 값이 닫는 괄호 일 때
        elif x in [')','}']: # ,']'
            # stack이 비어 있는지 확인
            if top == -1:
                # 비어있으면 0 반환
                return 0
            # stack에 값이 있으면 -1
            # 기호 확인, 개수 짝이 맞는지 확인
            if x == ')' and stack[top] == '(':
                    top -= 1
            elif x == '}' and stack[top] == '{':
                    top -= 1
            # 여는 기호의 수가 모자라면 0 반환
            else:
                return 0
    # 딱 떨어지면 1 아니면 0
    if top != -1:
        return 0
    else:
        return 1

# import sys
# sys.stdin = open("parentheses_check_input.txt", mode='r')
# sys.stdout = open("parentheses_check_output.txt", mode='w') 

T = int(input())

for time in range(1, T+1):
    # 입력받는 텍스트
    text = input()
    # 텍스트의 길이 만큼 스택 선언
    stack = [0] * len(text)

    result = check_parentheses(text, stack)

    print(f'#{time} {result}')