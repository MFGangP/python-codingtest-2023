T = int(input())

def calc_tree(T):
    val = 1
    time = 0
    while T >= val:
        val *= 2
        time += 1
    return 2 ** time

def in_order(T):
    global value
    if T <= N:
        in_order(T*2)  # 왼쪽 자식(서브트리)로 이동
        array[T] = value  # visit(T) T에서 할일 처리
        value += 1
        in_order(T*2+1) # 오른쪽 자식(서브트리)로 이동

for testcase in range(1, T+1):
    # 가장 큰 자연수
    N = int(input())
    # 간선의 수
    E = N-1
    # N 크기의 배열
    array = [0 for _ in range(calc_tree(N))]
    value = 1

    # 중위 순회 => LVR
    # 왼쪽 자식 : 2n, 오른쪽 자식 2n+1
    in_order(1)
    
    print(f"#{testcase} {array[1]} {array[N//2]}")