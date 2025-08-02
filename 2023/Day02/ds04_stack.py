# 스택 전체 구현

# global 변수
SIZE, stack, top = 0, [], -1

# 스택이 꽉 찼는지 여부 확인
def isStackFull():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓰겠다.
    if (top >= SIZE - 1):
        return True
    else:
        return False

# 스택이 비어있는지 여부 확인
def isStackEmpty():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓰겠다.
    if (top == - 1):        # top이 -1 이면 비었다는 소리니까
        return True         # true 반환
    else:                   # 아니면 안비었다는 소리니까
        return False        # False 반환

# 스택에 데이터 추가
def push(data):
    global SIZE, stack, top     # 전역변수를 그대로 함수에서도 쓰겠다.
    if (isStackFull()):         # 만약 스택이 다 찼으면
        print('Stack is Full')  # 다 찼다
        return                  #
    else:
        top += 1            # 안찼으면 top + 1 해주고
        stack[top] = data   # 데이터 추가

# 스택에서 데이터 추출
def pop():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓰겠다.
    if (isStackEmpty()):
        print('Stack is empty')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data

# top이 데이터 확인
def peek():
    global SIZE, stack, top # 전역변수를 그대로 함수에서도 쓰겠다.
    if isStackEmpty():
        print('Stack is Empty')
        return None
    else:
        return stack[top]

# 메인 엔트리
'''
if __name__ == '__main__':
    top = -1
    SIZE = int(input('스택 사이즈 입력 : '))
    stack = [None for _ in range(SIZE)]

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) : ')
        
        if select.lower() == 'x':   # 종료
            break
        elif select.lower() == 'i': # 데이터 삽입
            data = input('추가할 데이터를 입력해주세요 : ')
            push(data)
            print(f'스택 상태 : {stack}')
        elif select.lower() == 'e': # 데이터 추출
            data = pop()
            print(f'추출 데이터 : {data}')
            print(f'스택 상태 : {stack}')
        elif select.lower() == 'v': # 확인
            data == peek()
            print(f'확인 데이터 : {data}')
            print(f'스택 상태 : {stack}')
        else:
            continue
    print('스택 프로그램 종료')
'''