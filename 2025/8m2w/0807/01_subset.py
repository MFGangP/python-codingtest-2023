# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 
# 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.

# 해당하는 부분집합이 없는 경우 0을 출력한다. 
# 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. 
# ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 )

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
import sys
sys.stdin = open("subset_input.txt", mode='r')
sys.stdout = open("subset_output.txt", mode='w')

T = int(input())

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
for time in range(1, T+1):
    # N = 원소의 개수
    # K = 원소의 합 
    # 출력 = 원소의 합이 K인 부분 집합의 개수
    N, K = list(map(int, input().split()))
    # 부분 집합 리스트 - N 개의 원소를 가짐
    subset = [0] * N
    isInSubset = 0

    for i in range(1<<len(A)): # 1<<n : 부분 집합의 개수
        sum = 0
        sum_index = 0
        for j in range(len(A)): # A 원소의 수만큼 비트를 비교함
            if i & (1<<j): # i의 j번 비트가 1인경우
                sum += A[j]
                sum_index += 1
        # 합계가 K와 같고 인덱스 길이가 N과 같을 때
        if sum == K and sum_index == N:
            # isInSubset에 + 1
            isInSubset += 1

    print(f"#{time} {isInSubset}")
   
    # # 전달 받은 합을 비트로 만들기
    # for i in range(N-1, 0, -1):
    #     # 원소의 합을 2의N제곱으로 나눴을 때 1이 아닌 경우
    #     if K//(2**i) >= 1:
    #         # 값에 해당하는 비트에 1을 할당
    #         subset[(N-1)-i] = 1
    #         K = K%(2**i)
    #     # 원소의 합을 2로 나눴을 때 1인 경우 -> 연산 끝 0번
    #     elif K == 1:
    #         subset[(N-1)-i] = 1
    # print(*subset)