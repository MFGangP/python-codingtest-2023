import sys
sys.stdin = open("rotation_input.txt","r")
sys.stdout = open("rotation_output.txt","w")

T = int(input())

for testcase in range(1, T+1):
    # 숫자 갯수 N
    # 반복 횟수 M
    N, M = map(int, input().split())

    Q = [0] * (N+1)
    QC = list(map(int, input().split()))

    front = rear = 0
    # 새로 Q 배열에 할당해주려고 만듦
    for i in range(len(QC)):
        rear = (rear + 1) % (N + 1)
        Q[rear] = QC[i]

    for i in range(M):
        front = (front + 1) % (N + 1)
        rear = (rear + 1) % (N + 1)
        Q[rear] = Q[front]

    print(f"#{testcase} {Q[(front + 1) % (N+1)]}")
        