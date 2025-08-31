import sys
import math

sys.stdin = open("symmetric_saturated_binary_tree_input.txt","r")
sys.stdout = open("symmetric_saturated_binary_tree_output.txt","w")

T = int(input())

for testcase in range(1, T + 1):
    N = int(input())
    trees = list(map(int, input().split()))

    # 트리 높이 => 포화 이진 트리 노드 개수 = 2^h - 1
    # 높이가 h일 때, 최대의 노드의 개수인 (2^(h+1)-1)개의 노드를 가집니다. 
    # (예: 높이가 3일 때, 24−1=15개의 노드를 갖습니다.)
    tree_height = int(math.log2(N+1))
    result = True

    # 레벨별 검사
    for level in range(tree_height):
        start = 2**level - 1
        end = 2**(level+1) - 1
        nodes = trees[start:end]

        if nodes != nodes[::-1]:  # 좌우 대칭 검사
            result = False
            break

    print(f"#{testcase} {result}")
