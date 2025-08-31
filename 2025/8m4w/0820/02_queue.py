# front 와 rear를 사용해서 큐 만들기

# 큐 크기
N = 3

# 공백 상태의 큐를 생성
q = [0] * N

# front : 마지막에 삭제한 원소의 위치
# rear : 마지막에 삽입한 원소의 위치
front = rear = -1

# 1, 2, 3 삽입하기
for i in range(1, 4):
    # 가장 마지막에 삽입한 원소의 한 칸 뒤에 삽입을 해야한다.
    rear += 1
    # +1 한 위치에다가 넣어줘야 한다.
    q[rear] = i

print(q)

# 삭제해보기
for i in range(3):
    # 가장 마지막에 삭제한 원소의 위치 + 1에 있는 원소를 새로 삭제
    front += 1
    print(q[front], end=", ")
print()
# 리스트를 쓰고 있지만 우리가 큐 로 쓰자고 했기 때문에 이건 큐다.
# front, rear 가 같으니까 비어있다 생각해야한다
print(q, front, rear)    

# # 큐의 포화상태 예시
# rear += 1
# q[rear] = 5

# front랑 rear 당겨서 쓰면 안되나?
# 100만개 배열이라 생각하면 기하급수적으로 해야할 횟수가 늘어난다.