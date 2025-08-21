import sys
sys.stdin = open("balloon_pang_bonus_2_input.txt", mode='r')
sys.stdout = open("balloon_pang_bonus_2_output.txt", mode='w')

T = int(input())

for testcase in range(1, T+1):
    # N = 배열 크기
    N = int(input())
    # Aji = NxN 크기 배열
    Aji = [list(map(int, input().split())) for _ in range(N)]
    max_count = 0

    for i in range(N):
        for j in range(N):
            # 행 전체 더하기 + 열 전체 더하기
            count = sum(Aji[i]) + sum(Aji[x][j] for x in range(N)) - Aji[i][j]
            
            # 모든 방향 순회가 끝나고 값 체크
            if max_count < count:
                max_count = count

    print(f"#{testcase} {max_count}")