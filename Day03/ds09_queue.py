# 큐 구현

# 전역변수
SIZE = 0
queue = []
front = rear = -1

# Queue Full Check
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear != SIZE - 1):
        return False
    elif(rear == SIZE - 1) and (front == - 1):
        return True
    else:
        # dequeue를 한 뒤에 비어있는 빈칸으로 데이터 당기기
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

# Queue Empty Check
def isQueueEmpty():
    global SIZE, queue, front, rear
    if (rear == SIZE):
        return True
    else:
        return False

# Queue EnQueue

def enQueue(data):  # Queue Data 추가
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is Full')
    else:   # else 있어서 리턴 시킬 필요가 없음
        rear += 1
        queue[rear] = data

def deQueue():  # Queue Data 추출
    global SIZE, queue, front, rear
    if isQueueEmpty():  
        print('Queue is Empty')
        return None # 비었으니까 아무것도 없음
    else:
        front += 1  # 빼낼거니까 1증가
        data = queue[front] # 데이터에 넘겨주고
        queue[front] = None # 스택 안은 None 으로 만들기

        # 삭제와 동시에 한 칸씩 당기기
        for i in range(front+1, SIZE):  # 맨앞에서 부터 큐 크기 끝까지
            queue[i-1] = queue[i]   # 0번부터 차례대로 한칸씩 당긴다
            queue[i] = None # 당기고 난 뒤에는 None으로 비운다.
        front -= 1  # 당기고나서 복구
        rear -= 1   
        return data # 데이터 리턴

def peek(): # Queue front + 1 위치값 확인
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return None
    else:
        return queue[front+1]

# 메인 엔트리

if __name__ == '__main__':
    SIZE = int(input('큐 사이즈 입력 : '))
    queue = [None for _ in range(SIZE)] 
    # 대문자는 상수로 안바꾼다 생각하고 지정하는거다 이렇게 안쓴다

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) : ')
        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('입력데이터 >> ')
            enQueue(data)
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'e':
            data = deQueue()
            print(f'추출 데이터 : {data}')
            print(f'큐 상태 : {queue}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인 데이터 : {data}')
            print(f'큐 상태 : {queue}')
                
        else:
            continue

    print('큐 프로그램 종료')