import sys
sys.stdin = open("climb_the_ladder_input.txt", mode='r')

def find_left_item(ladder, x, y):
    # 다음 i, j
    nx, ny = x, y-1
    # 좌, 우, 상에 값이 있다면.
    if ladder[nx][ny] == 1:
        # 해당 방향 탐색 계속
        x, y = find_left_item(ladder, nx, ny)
        return x, y
    # 진행하던 방향에 값이 없다면
    else:
        # 현재 노드 반환
        return x-1, y

def find_right_item(ladder, x, y):
    # 다음 i, j
    nx, ny = x, y+1
    # 좌, 우, 상에 값이 있다면.
    if ladder[nx][ny] == 1:
        # 해당 방향 탐색 계속
        x, y = find_right_item(ladder, nx, ny)
        return x, y
    # 진행하던 방향에 값이 없다면
    else:
        # 현재 노드 반환
        return x-1, y

for _ in range(1, 11):
    time = int(input())
    x = 0
    y = 0
    N = 100
    ladder = [list(map(int, input().split())) for _ in range(N)]
    # 사다리에서 2의 값을 가진 시작점을 찾아야한다.
    for i in range(N-1, 0, -1):
        for j in range(N-1, 0, -1):
            if ladder[i][j] == 2:
                x = i
                y = j
                break
        break
    # 시작 점 x, y를 찾았으니 
    for i in range(N):
        for j in range(N):
            # 일단 앞으로 전진
            sdi, sdj = -1, 0
            ldi, ldj = 0, -1
            rdi, rdj = 0, 1
            for c in range(ladder[x][y]): 
                ni, nj = i+sdi*c, j+sdj*c
                if x == 0:
                    break
                elif 0<=ni<N and 0<=nj<N: 
                    # 왼쪽에 탐색해야할 배열이 있다면.
                    if ladder[x+ldi][y+ldj] == 1:
                        x, y = find_left_item(ladder, x, y)
                    # 오른쪽에 탐색해야할 배열이 있다면.
                    elif ladder[x+rdi][y+rdj] == 1:
                        x, y = find_right_item(ladder, x, y)
                    # 앞에 탐색해야할 배열이 있다면.
                    elif ladder[x+sdi][y+sdj] == 1:
                        x, y = x+sdi, y+sdj    
        if x == 0:
            break
    print(f"#{time} {y}")
