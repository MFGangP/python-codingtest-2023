import sys
sys.stdin = open("operations_input.txt", "r")
sys.stdout = open("operations_output.txt", "w")

def post_order(T):
    if T:
        # 좌우에 방문할 노드가 있을 경우
        if c_left[T] and c_right[T]:
            lc = post_order(c_left[T])
            rc = post_order(c_right[T])
            value = val[T]

            if value == "*":
                return lc * rc
            elif value == "/":
                return lc // rc
            elif value == "+":
                return lc + rc
            elif value == "-":
                return lc - rc
        # 없는 경우
        else:
            return val[T]
    else:
        return 0

# 테스트 케이스는 총 10개
for testcase in range(1, 11):
    # 정점의 개수
    N = int(input())
    
    idx = [0] * (N+1)
    val = [0] * (N+1)
    c_left = [0] * (N+1)
    c_right = [0] * (N+1)

    result = 0

    for node_num in range(N):
        node_list = list(input().split())
        # 입력 값이 4개 일 경우
        if len(node_list) == 4:
            idx[int(node_list[0])] = int(node_list[0])
            val[int(node_list[0])] = node_list[1]
            c_left[int(node_list[0])] = int(node_list[2])
            c_right[int(node_list[0])] = int(node_list[3])
        # 입력 값이 2개일 경우
        else:
            idx[int(node_list[0])] = int(node_list[0])
            val[int(node_list[0])] = int(node_list[1])

    result = post_order(1)

    print(f"#{testcase} {int(result)}")