# 상하좌우 이동 O => 델타 사용
import sys
sys.stdin = open("rolling_ball_input.txt", mode='r')
sys.stdout = open("rolling_ball_output.txt", mode='w') 

def dfs(ni, nj, move_count):            
        # 좌표 범위 확인
        # ni, nj가 범위 안에 있으면 계속
        if 0<=ni<N and 0<=nj<N:
            # 현재 좌표 값이랑 비교해서 다음 값이 더 작을 경우
            if array[ni][nj] < array[i][j]:
                # 만약 다음 값이 기존에 저장되어있던 x,y와 비교했을 때
                # 값보다 작다면 교체
                if array[ni][nj] < array[x][y]:
                    x,y = ni,nj
                    move_count += 1
                    dfs(ni, nj, move_count)
        else:
            return move_count

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    # 좌표 값을 저장 할 변수 x, y
    x = y = 0

    # 이동 횟수 
    max_move_count = 0
    # N x N 배열
    array = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            move_count = 0
            # 이동 방향은 상 하 좌 우
            for di, dj in [[0, -1], [0, 1], [-1, 0], [0, -1]]:
                ni, nj = i+di, j+dj
                move_count = dfs(ni, nj, move_count)

        # 최대 이동 거리가 현재 이동 거리보다 작다면
    if max_move_count < move_count:
        max_move_count = move_count

    print(f"#{testcase} {max_move_count}")

# 공 굴리기 게임을 하려고 한다.
# N * N 크기의 격자판이 있다. 플레이어에게는 공을 굴릴 기회가 1번 주어진다.
# 플레이어는 격자판에서 공을 최대한 많이 이동시키는 것이 목표이다.

# 격자판의 각 칸에는 정수가 하나씩 적혀 있다.
# 공은 어떤 칸에서 시작해서 상하좌우로 이동할 수 있다.
# 단, 이동을 할때 현재 칸보다 숫자가 작은 칸으로만 이동할 수 있고, 
# 상하좌우중 가장 작은 숫자가 있는 칸으로만 이동한다.

# 상하좌우중 가장 작은 숫자가 같다면, 상 => 하 => 좌 => 우 순서로 우선권을 가진다.
# 예를 들어, 위와 아래에 가장 작은수가 같은게 있을 경우 위쪽으로 가게 된다.
# 상하좌우에 공이 있는 칸보다 숫자가 작은 칸이 없으면 공은 이동을 멈춘다.

# 격자판 정보가 주어질때 공을 최대 몇 칸 굴릴 수 있는지 구하는 프로그램을 작성하시오.

# 예제)

# 위와 같은 예제에서 53에서 시작해서 53-49-32-27-26-19 로 최대 6칸 이동 가능하다.

# 제한사항)
# 5 <= N <= 10
# 1 <= 각 칸에 적혀있는 숫자 <= 99