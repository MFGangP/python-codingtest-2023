import sys
sys.stdin = open("delete_repeated_charactors_input.txt", mode='r')
sys.stdout = open("delete_repeated_charactors_output.txt", mode='w') 

def check_repeated_character(stack, text, top):
    # 글자 개수만큼 반복
    for char in text:
        # 현재 스텍 top 값이 char값이랑 다르거나
        # 스택이 비어있다면.
        if top == -1 or stack[top] != char:
            top += 1
            # top +1 해준 뒤 해당 값 대입
            stack[top] = char
        # 현재 스텍 top 값이 char랑 값이 똑같다면
        elif stack[top] == char:
            top -= 1
    return top + 1
        
T = int(input())

for time in range(1, T+1):
    text = list(input())
    top = -1
    # 입력 글자
    stack = [0] * len(text)

    result = check_repeated_character(stack, text, top)

    print(f"#{time} {result}")        
