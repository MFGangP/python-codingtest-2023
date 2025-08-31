'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''
# 테케
T = int(input())

def pre_order(T):
    global sub_tree_sum
    if T:
        sub_tree_sum += 1
        # 왼쪽 노드
        pre_order(c_left[T])
        # 오른쪽 노드
        pre_order(c_right[T])

# 첫 줄에 간선의 개수 E와 N이 주어지고, 
# 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
for testcase in range(1, T+1):
    # E : 간선 개수, N : 시작 노드
    E, N = map(int, input().split())

    nodes = list(map(int, input().split()))
    # 왼쪽, 오른쪽 자식 노드 리스트
    c_left = [0] * (E+2)
    c_right = [0] * (E+2)

    sub_tree_sum = 0

    # 입력 받은 노드 개수만큼 돌면서
    # 부모 노드 자식 노드 분류 0~N
    for i in range(E):
        # 부모 노드는 앞
        p = nodes[i*2]
        # 자식 노드는 뒤
        c = nodes[i*2+1]
        # left에 값이 채워지지 않았다면
        if c_left[p] == 0:
            # left에 노드 대입
            c_left[p] = c
        # left에 다른 값이 들어가있다면
        else:
            c_right[p] = c

    pre_order(N)

    print(f"#{testcase} {sub_tree_sum}")