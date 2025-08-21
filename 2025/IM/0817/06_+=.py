import sys
sys.stdin = open("+=_input.txt", mode='r')
sys.stdout = open("+=_output.txt", mode='w')

T = int(input())

for _ in range(1, T+1):
    A, B, N = map(int, input().split())
    cnt = 0

    while max(A, B) <= N:
        if A < B:
            A += B
        else:
            B += A
        cnt += 1
        
    print(cnt)
