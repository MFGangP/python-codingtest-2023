import sys
sys.stdin = open("password_generator_input.txt","r")
sys.stdout = open("password_generator_output.txt","w")

# 테스트 케이스 10개
for _ in range(1, 11):
    # 테스트 케이스 번호
    testcase = int(input())

    # 입력 데이터
    Datas = list(map(int, input().split()))

    # testcase
    N = len(Datas)

    # 큐 front, rear 초기화
    front = rear = 0

    # 원형 큐 생성
    que = [0] * (N+1)

    # 결과 값
    result = []

    # que 데이터 삽입
    for i in range(len(Datas)):
        que[i+1] = Datas[i]

    # 감소 시킬 수
    i = 1
    while True:
        # i 가 5보다 커지면
        if i > 5:
            # i 초기화
            i = 1
        # rear 값 갱신
        rear = (rear + 1) % (N + 1)
        # front가 있는 곳으로 포인터가 돌아오면
        if rear == 0:
            # 1번으로 이동
            rear += 1
        # 큐 rear 값 갱신
        que[rear] -= i
        # 증가량 수정
        i += 1
        # 갱신 한 값이 0보다 작거나 같은 경우
        if que[rear] <= 0:
            # 값은 0으로 고정
            que[rear] = 0
            # 0인 값을 뒤로 보낸 뒤 순서대로 값 출력
            for j in range(N):
                # rear가 N이랑 같은 경우 - 1 더하면 0으로 가는 경우
                if rear == N:
                    # rear + 1 -> 0으로 만들어서 1부터 시작하게 만듦
                    rear += 1
                rear = (rear + 1) % (N + 1)
                result.append(que[rear])
            print(f"#{testcase} ", end="")
            print(*result)
            # 반복문 종료
            break
        # 다음 계산
        continue