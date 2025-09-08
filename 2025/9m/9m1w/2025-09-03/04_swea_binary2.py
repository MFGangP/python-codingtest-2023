import sys
sys.stdin = open('swea_binary2_input.txt', "r")
sys.stdout = open('swea_binary2_output.txt', "w")

T = int(input())

def binary_decimal(idx, n, decimal_list : list):
    # decimal_list 소수점 계산이 
    # 12번이 넘었을 때 남은 수가 0으로 나눠졌으면 True
    # 실패했다면 False
    if idx >= 13:
        return n == 0
    
    # 계산 중간에 n이 0이 되면 성공(True)
    if n == 0:
        return True

    # 뺄 수가 없는 경우
    # 다음 지수 계산으로 넘기기
    if n < 2**(-idx):
        decimal_list[idx] = 0
        return binary_decimal(idx+1, n, decimal_list)

    # 이번 지수 계산으로 빼지는 경우
    # n >= 2**-idx
    else:
        calc_val = n - 2**(-idx)
        decimal_list[idx] = 1
        return binary_decimal(idx+1, calc_val, decimal_list)


for tc in range(1, T+1):
    # 소수 1개
    N = float(input())
    # 소수점 12자리 까지 2^1
    decimal_list = [0 for _ in range(13)]

    result = binary_decimal(1, N, decimal_list)

    # 12자리 넘겨서 0을 만들지못했다면 overflow
    if result == False:
        print(f"#{tc} overflow")
    # 12자리 안으로 0만들기에 성공했다면.
    else:
        # 결과가 0.5처럼 짧을 경우, 
        # 불필요한 0을 출력하지 않기 위해 마지막 1의 위치를 찾음
        # 왜냐? 소수니까 뒤에 0나올 일이 없음. [중요!]
        last_idx = 0
        for i in range(12, 0, -1):
            if decimal_list[i] == 1:
                last_idx = i
                break

        print(f"#{tc} ", end="")
        for idx in range(1, last_idx+1):
            print(f"{decimal_list[idx]}", end="")
        print()