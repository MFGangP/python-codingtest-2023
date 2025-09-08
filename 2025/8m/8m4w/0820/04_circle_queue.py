N = 10

# 원형 큐 초기화 
CQ = [0] * 10
front = rear = 0
# 원형 큐는 front를 위한 자리 1개를 비워둔다.

def is_full():
    return (rear + 1) % N == front

def is_empty():
    return rear == front 

for i in range(1, 11):
    # 이게 없으면 front 랑 rear가 같아지고 그러면
    # 이게 다 찬건지 비어있는건지 알 수가 없어진다.
    if not is_full():
        rear = (rear + 1) % N
        CQ[rear] = i

print(CQ)

for i in range(9):
    front = (front + 1) % N
    print(CQ[front], end=", ")

print()

# front를 위해 비워둔 자리는 삭제할 때 마다 바뀐다.