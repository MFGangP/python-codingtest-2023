import sys
sys.stdin = open("two_number_sequences_input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    result = float("-inf")

    N, M = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    if N < M:
        for i in range(M-N+1):        
            sum_result = 0
            for j in range(N):
                sum_result += B[i+j]*A[j]
            if result < sum_result:
                result = sum_result
    else:
        for i in range(N-M+1):        
            sum_result = 0
            for j in range(M):
                sum_result += A[i+j]*B[j]
            if result < sum_result:
                result = sum_result

    print(f"#{tc} {result}")