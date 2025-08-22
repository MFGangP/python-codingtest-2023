import sys
sys.stdin = open("in_order_input.txt","r")
sys.stdout = open("in_order_output.txt","w")

def pre_order(T):
    global sub_tree_sum
    if T:
        # 왼쪽 노드
        pre_order(c_left[T])
        # 중위 노드
        sub_tree_sum.append(char_list[T])
        # 오른쪽 노드
        pre_order(c_right[T])

for testcase in range(1, 11):
    # 첫 줄에 간선의 개수 E와 N이 주어지고, 
    # 다음 줄에 E개의 부모 자식 노드 번호 쌍이 주어진다.
    N = int(input())

    # 글자 정보 담을 리스트
    char_list = [0] * (N+1)

    # 왼쪽, 오른쪽 자식 노드 리스트
    c_left = [0] * (N+1)
    c_right = [0] * (N+1)
    
    sub_tree_sum = []
    # 정점 수 만큼 반복
    for i in range(N):
        # 트리가 갖는 정점의 총 수
        datas = list(input().split())
        # 부모 노드는 앞
        p = int(datas[0])
        # 들어온 노드 정보에 자식 노드가 2개 있다면
        if len(datas) > 3:
            # 자식 노드는 뒤
            cl = int(datas[2])
            cr = int(datas[3])       
        # 들어온 노드 정보에 자식 노드가 1개 있다면
        elif len(datas) > 2:       
        # 자식 노드는 뒤
            cl = int(datas[2])         
        if cl:
            # left에 노드 대입
            c_left[p] = cl
            cl = 0
        if cr:
            # right에 노드 대입
            c_right[p] = cr
            cr = 0
        char_list[p] = datas[1]

    pre_order(1)
    print(f"#{testcase} ")
    print(*sub_tree_sum, sep="")