import sys
sys.stdin = open("max_min_len_input.txt", mode='r')
sys.stdout = open("max_min_len_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    # N = 리스트 크기
    N = int(input())
    # 숫자 리스트
    ai = list(map(int, input().split()))

    max_index = 0
    min_index = 0

    max_value = ai[0]
    min_value = ai[0]

    for i in range(len(ai)):
        # 최소값 갱신
        if ai[i] < min_value:
            min_value = ai[i]
            min_index = i
        # 최대 값 갱신
        if ai[i] >= max_value:
            max_value = ai[i]
            max_index = i

    print(f"#{testcase} {abs(max_index - min_index)}") 
