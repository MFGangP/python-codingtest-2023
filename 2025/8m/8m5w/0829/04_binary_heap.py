import heapq
import sys
sys.stdin = open("binary_heap_input.txt", "r")
sys.stdout = open("binary_heap_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    # 노드 개수 
    N = int(input())

    heap = [0] * (N+1)

    last = 0
    result = 0

    def enq(item):
        global last

        last += 1
        heap[last] = item

        child = last
        parent = last // 2
        
        # 자식이 부모보다 작다면 자리 바꾸기
        while parent != 0 and heap[child] < heap[parent]:
            heap[child], heap[parent] = heap[parent], heap[child]
            # 부모의 부모가 새로운 부모가 되고    
            child = parent
            parent = child // 2

    # 1000000이하인 서로 다른 N개의 자연수
    values = list(map(int, input().split()))

    p_list = []
    # 힙에 값은 순서대로 집어넣어야한다.
    for i in range(len(values)):
        enq(values[i])
    
    while last != 0:
        last = last//2
        result += heap[last]

    print(f"#{testcase} {result}")