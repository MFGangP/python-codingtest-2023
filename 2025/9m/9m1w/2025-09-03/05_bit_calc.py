import sys
sys.stdin = open("bit_calc_input.txt","r")
sys.stdout = open("bit_calc_output.txt","w")

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # N: 마지막 N개 비트 
    # M: 이진수로 표현할 정수
    N, M = map(int, input().split())
    # N개의 1로 이루어진 비트를 만들기 위해 1을 N번 밀고 1을 빼준다
    mask = (1 << N) - 1
    # AND 연산으로 N개의 1로 이루어진 비트와 비교
    if (M & mask) == mask:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")