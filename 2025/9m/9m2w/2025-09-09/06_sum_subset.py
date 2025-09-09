import sys
sys.stdin = open("sum_subset_input.txt", "r")
sys.stdout = open("sum_subset_output.txt", "w")

T = int(input())

# 집합 A는 항상 {1, 2, ..., 12}로 고정
A = list(range(1, 13))
n = len(A) # n = 12

for tc in range(1, T + 1):
    # N: 원소의 수, K: 원소의 합
    N, K = map(int, input().split())
    
    count = 0 # 조건을 만족하는 부분집합의 개수

    # 모든 부분집합을 순회 (0부터 2^12 - 1 까지)
    # 1 << n 은 2^n 을 의미
    for i in range(1 << n):
        subset_sum = 0
        element_count = 0
        
        # 현재 부분집합(i)에 어떤 원소가 포함되는지 확인
        for j in range(n):
            # i의 j번째 비트가 1인지 확인
            if i & (1 << j):
                # j번째 비트가 1이면, A[j] 원소를 부분집합에 포함
                subset_sum += A[j]
                element_count += 1
        
        # 원소의 개수가 N개이고, 원소의 합이 K이면 카운트 증가
        if element_count == N and subset_sum == K:
            count += 1
            
    print(f"#{tc} {count}")