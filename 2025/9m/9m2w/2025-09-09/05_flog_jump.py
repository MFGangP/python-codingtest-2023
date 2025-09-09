import sys
sys.stdin = open("flog_jump_input.txt", "r")
sys.stdout = open("flog_jump_output.txt", "w")

T = int(input())

def solve(corrent_value):
    # 탈출 조건
    # N보다 값이 더 커진 경우 or 끝에 도착한 경우
    if corrent_value >= N:
        return N
    # 범위 안이면
    else:
        # 나뭇잎이 존재하고 내가 뛸 자리가 범위 안인 경우
        if array[corrent_value] == 1:
            return solve(corrent_value + K)
        # 어쩔 수 없이 뛰어야하는 경우
        else:
            # 내 앞자리에 뛸 자리가 있는지 확인
            for i in range(-K+1, 0):
                if array[corrent_value + i] == 1:
                    return solve(corrent_value + i)
                else:
                    continue
            # 없으면 최대 값 반환
            else:
                if corrent_value + 1 < N:
                    return corrent_value + 1
                else:
                    return N

for tc in range(1, T+1):
    # N 물웅덩이 길이
    # K 최대로 점프할 수 있는 거리
    N, K = map(int, input().split())
    array = list(map(int, input().split()))
    # 물 웅덩이는 0 부터
    c_val = 0

    # 현재 위치가 물웅덩이 보다 작을 때까지 반복
    result = solve(c_val)
    print(f"#{tc} {result}")