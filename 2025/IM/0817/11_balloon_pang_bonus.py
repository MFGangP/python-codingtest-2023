import sys
sys.stdin = open("balloon_pang_bonus_input.txt", mode='r')
sys.stdout = open("balloon_pang_bonus_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    # N = 배열 크기
    N = int(input())
    # Aji = NxN 크기 배열
    Aji = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0
    min_count = N * N
    for i in range(N):
        for j in range(N):
            count = sum(Aji[i]) + sum(Aji[x][j] for x in range(N)) - Aji[i][j]
            max_count = max(max_count, count)
            min_count = min(min_count, count)

    print(f"#{testcase} {max_count - min_count}")

    