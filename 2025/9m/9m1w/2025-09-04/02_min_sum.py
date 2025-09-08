import sys
sys.stdin = open("min_sum_input.txt", "r")
sys.stdout = open("min_sum_output.txt", "w")

T = int(input())
# 우 하
di = [0, 1]
dj = [1, 0]

# 현재 위치 (i, j) i는 행 번호, j는 열 번호
# (0, 0) => 우 or 하 이동 반복 => (N-1, N-1)
def solve(i, j, total):
    global result

    total += matrix[i][j]
    # 종료 - 도착 지점을 우리는 알고 있다.
    # (N-1, N-1)
    if (i, j) == (N-1, N-1):
        # 도착했으니 합을 구하고
        # 그 합이 최소인가?
        # 최소 값이 total 보다 큰경우
        if result > total:
            result = total
        return result

    # 재귀 호출(다음 단계)
    # 방향 선택지 2개 => 재귀 호출도 2개
    # 오른쪽 or 아래 - 범위 체크도 같이

    for c in range(2):
        ni, nj = i+di[c], j+dj[c]
        if 0<=ni<N and 0<=nj<N:
            solve(ni, nj, total)

for tc in range(1, T+1):
    N = int(input())
    # NxN
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # 문제에서 원하는 답: 합이 최소가 되도록
    # 최대값
    result = float("inf")

    # 재귀 호출
    solve(0, 0, 0)

    print(f"#{tc} {result}")