import sys
sys.stdin = open("pizza_input.txt","r")
sys.stdout = open("pizza_output.txt","w")

# 테스트 케이스
T = int(input())

def is_full(front, rear):
    return (rear + 1) % (N + 1) == front

def is_empty(front, rear):
    return rear == front

for testcase in range(1, T+1):
    # N = 화덕 크기
    # M = 피자 개수
    N, M = list(map(int, input().split()))

    # 치즈 양
    Ci = list(map(int, input().split()))

    # front, rear 변수
    pizza_front = pizza_rear = 0
    oven_front = oven_rear = 0
    
    # 피자 선형 큐
    pizza_queue = [0] * (M + 1)
    # 화덕 원형 큐
    oven_circle_queue = [0] * (N + 1)
    # 피자 인덱스 큐 
    oven_pizza_index_queue = [0] * (N + 1)
    # 피자 선형 큐에서 꺼내올 피자의 여부
    is_last_pizza = False

    # 피자 선형 큐에 치즈 양 등록
    for i in range(len(Ci)):
        pizza_rear += 1
        pizza_queue[pizza_rear] = Ci[i]

    # 오븐 자리 수만큼 피자 선형 큐에서 빼오기
    for i in range(1, N+1):
        pizza_front += 1
        oven_rear += 1
        oven_circle_queue[i] = pizza_queue[pizza_front]
        oven_pizza_index_queue[i] = pizza_front

    # 화덕에 피자가 N 개만큼 꾸준히 들어가야한다.
    while True:
        # 화덕 한칸 이동
        oven_rear = (oven_rear + 1) % (N + 1)
        # 화덕이 한바퀴 돌아서 초기 상태로 돌아왔다면
        if is_empty(oven_front, oven_rear):
            # 한칸 추가로 이동
            oven_rear = (oven_rear + 1) % (N + 1)
        # 한바퀴 돈 피자 치즈 양 // 2
        oven_circle_queue[oven_rear] = oven_circle_queue[oven_rear] // 2
        # 치즈가 다 녹았다면
        if oven_circle_queue[oven_rear] == 0:
            # 피자 소모가 끝났다면
            if is_last_pizza:
                pizza_count = []
                # 오븐 안에 있는 피자 상태 확인
                for i in range(len(oven_circle_queue)):
                    # 오븐 안에서 도는 피자의 치즈 양이 0보다 크다면
                    if oven_circle_queue[i] > 0:
                        # 피자 인덱스 큐에 동일한 인덱스 값을 리스트에 추가
                        pizza_count.append(oven_pizza_index_queue[i])
                # 피자 인덱스 큐 갯수가 1개 초과면 continue
                if len(pizza_count) > 1:
                    continue
                # 피자 인덱스 큐 갯수가 하나라면
                elif len(pizza_count) == 1:
                    # 프린트하고 테스트 케이스 종료
                    print(f"#{testcase} {pizza_count.pop()}")
                    break
            # 더 이상 꺼내올 피자가 없다면
            if is_empty(pizza_front, pizza_rear):
                # 마지막 피자 알려주는 Bool 값 True로 바꿔주기
                is_last_pizza = True
                continue
            # 피자 front + 1
            pizza_front += 1
            # 오븐 큐에 피자 추가
            oven_circle_queue[oven_rear] = pizza_queue[pizza_front]
            # 피자 인덱스 큐에 피자 인덱스 추가
            oven_pizza_index_queue[oven_rear] = pizza_front