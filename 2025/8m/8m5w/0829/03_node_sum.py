import sys
sys.stdin = open("node_sum_input.txt", "r")
sys.stdout = open("node_sum_output.txt", "w")

T = int(input())
# 3
# 5 3 2
# 4 1
# 5 2
# 3 3
# 10 5 2
# 8 42
# 9 468
# 10 335
# 6 501
# 7 170

#1 3
#2 845
#3 1801

def post_order(T):
    # T 값이 0이라면, 
    # => 0이 아니면 reaf 노드니까 체크 할 필요 없다
    # 어차피 마지막 노드인데 체크 웨함?
    # T가 0이다 라는 말은 0 == False 이기 때문.
    # 값이 없다는 소리
    
    # 인덱스 안이라면
    if T < len(p_list):
        if p_list[T] == -1:
            # 왼쪽 자식
            left_value = post_order(T*2)
            # 오른쪽 자식
            right_value = post_order(T*2+1)
            # 중위 값
            # 현재 내가 있는 노드 값은 
            # 왼쪽 + 오른쪽 노드 값
            p_list[T] = left_value + right_value
            return p_list[T]
        else:
            return p_list[T]
    # 인덱스 밖이라면 탈출
    else:
        # 0 리턴
        return 0

for testcase in range(1, T+1):
    # 노드의 개수 N
    # 리프 노드의 개수 M
    # 출력할 노드의 번호 L
    N, M, L = map(int, input().split())

    p_list = [-1] * (N+1)

    for _ in range(M):
        # 부모 노드, 자식 노드 입력
        p, c = map(int, input().split())
        # 부모 노드 기준으로 값이 있는지 체크
        if p_list[p] == 0:
            p_list[p] = c
        # 왼쪽 노드에 값이 있으면 오른쪽 노드에 추가
        else:
            p_list[p] = c

    # 이제 후위순회 돌면서 값을 더해주면 된다.
    # post_order에 흠.... 1번 넣어주면 되겠네
    post_order(1)

    print(f"#{testcase} {p_list[L]}")