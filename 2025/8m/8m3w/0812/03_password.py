import sys
sys.stdin = open("password_input.txt", mode='r')
sys.stdout = open("password_output.txt", mode='w') 

def password_logic(stack, password, top):
    for char in password:
        # 만약 스택이 빈값이거나 top 값이 같지 않은 경우
        if top == -1 or stack[top] != char:
            top += 1
            stack[top] = char
        # 스택 값과 문자가 같은 경우 
        elif stack[top] == char:
            top -= 1
    return ''.join(stack[0:top + 1])

for time in range(1, 11):
    # 입력받는 텍스트
    N, password = input().split()
    stack = [0] * int(N)
    top = -1

    result = password_logic(stack, password, top)
    print(f"#{time} {result}")