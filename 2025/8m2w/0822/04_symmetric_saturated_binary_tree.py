import sys
sys.stdin = open("symmetric_saturated_binary_tree_input.txt","r")
sys.stdout = open("symmetric_saturated_binary_tree_output.txt","w")

T = int(input())

for testcase in range(1, T+1):
    # N : 트리의 크기
    N = int(input())

    trees = list(map(int, input().split()))

    is_same_tree = True

    # 한 칸당 2**n 씩 노드 늘어남
    for i in range((N//2)):
        # 0, 1, 3, 7
        # 2**n 법칙으로 레벨별 요소 모두 꺼내기
        if trees[(2**i)-1:2**(i+1)-1] != trees[(2**i)-1:2**(i+1)-1][::-1]:
            # 뒤집었을 때 다르면 False
            is_same_tree = False
            break
        else:
            continue
    
    print(f"#{testcase} {is_same_tree}")