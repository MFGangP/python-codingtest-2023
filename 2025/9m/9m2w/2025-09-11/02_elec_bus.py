import sys
sys.stdin = open("elec_bus_input.txt", "r")
sys.stdout = open("elec_bus_output.txt", "w") 

T = int(input())

# 교체 횟수
def solve(total):
    global result

    # 현재 배터리로 갈 수 있는 도착지가 마지막 종점 까지 왔다면
    if total + M[total] >= N:
        return 0
    # 배터리 충전으로 갈 수 있는 최대 정류장 길이
    max_length = total + M[total]

    # 다음 정류장 갱신을 위한 변수 (인덱스로 따지기 때문에 -1)
    next_bus_stop = -1
    # 범위 내 가장 멀리 갈 수 있는 정류장 값
    fast_length = 0

    # 다음 정류장을 찾기위해 (범위 : +1 ~ 최대 범위)
    for next_stop in range(total+1, max_length+1):
        # 다음 정류장 충전으로 갈 수 있는 최대치
        most_range_bus_stop = next_stop + M[next_stop]
        # 최대치가 이전 값들보다 더 길다면
        if most_range_bus_stop > fast_length:
            # 가장 멀리가는 정류장 갱신
            fast_length = most_range_bus_stop
            # 다음 정류장 값 갱신
            next_bus_stop = next_stop

    # 배터리 최대로 다 쓴다음 충전하는 방법.
    return 1 + solve(next_bus_stop)


for tc in range(1, T+1):
    # N : 정류장 수, M : 정류장 별 배터리 용량 N-1개
    A = list(map(int, input().split()))
    # 첫번째 값은 정류장 수
    N = A[0]-1
    # 실제 정류장은 N-1 값
    M = A[1:]

    result = float("inf")

    result = solve(0)

    print(f"#{tc} {result}")