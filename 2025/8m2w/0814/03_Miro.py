T = int(input())

# si, sj : 시작점 좌표
def DFS(si, sj):
    # 중복체크 배열도 2차원
    visited = [[0] * N for _ in range(N)]
    # (x, y)를 탐색한 적 있다. => visited[x][y] = 1
    # (w, z)를 탐색한 적 없다. => visited[w][z] = 0

    stack = []

    # 현재 탐색중인 위치
    vi, vj = si, sj

    # 시작 지점 방문 체크
    visited[vi][vj] = 1

    # 탐색 시작
    while True:
        # 현재 위치 디버깅용
        # for i in range(N):
        #     for j in range(N):
        #         if (i,j) == (vi,vj):
        #             print("*",end="")
        #         else:
        #             print(maze[i][j],end="")
        #     print()
        # print("==================")

        # 현재 정점 위치 (vi, vj)에서 탐색
        # 현재 위치가 도착점인가? 검사
        if miro[vi][vj] == 3:
            # 도착점에 왔으면 더이상 진행 될 필요 없음
            return 1
 
        # (vi, vj)에서 갈 수 있는 다른 위치 찾기
        # (ni, nj) : 다른 위치
        # 4방향
        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            # d 방향으로 갔을 떄 다른 위치 ni, nj 구하기
            ni = vi + di
            nj = vj + dj
            # 1.(ni,nj)가 범위 안에 있고,
            # 2.miro(ni,nj)가 벽이 아니며,
            # 3.visited(ni,nj)가 방문한 적이 없는 곳이면
            if ((0<=ni<N and 0<=nj<N) and
                (miro[ni][nj] != 1) and 
                (not visited[ni][nj])):
                # (ni,nj)로 이동할 것이기 때문에 현재 위치(vi,vj)를
                # 스택에 저장
                stack.append((vi,vj))
                # 방문 
                visited[ni][nj] = 1
                vi, vj = ni, nj
                # 내가 갈 곳을 정했으면 다른데는 안봐도 된다.
                break
        # for문에 걸어줘야한다.
        else:
            # 못찾았다면 다른 위치로 이동
            # 중간에 break를 한 적이 없다 => 갈 수 있는 방향이 없다.
            # 길이 없다는 거니까 돌아가자.
            # 어디로 돌아가는데? => 그 위치는 스택이 알고있다.
            if stack:
                vi, vj = stack.pop()
            # 만약 스택도 비어있었다
            else:
                break
    # 탐색을 다 마쳤는데 3을 발견 못하면 return 0
    return 0

def DFS2(si, sj):
    # 현재 위치 si, sj 방문 체크
    visited2[si][sj] = 1
    # 재귀 호출 종료(도착 지점을 찾음)
    if miro[si][sj] == 3:
        # 다른 방향이 있어도 안본다
        return 1
    else:
        # 못찾았다면 다른 위치로 이동(si,sj)를 상하좌우로 이동시켜서
        for di, dj in [[-1,0], [1,0], [0,-1], [0,1]]:
            ni, nj = si + di, sj+dj
            if ((0<=ni<N and 0<=nj<N) and 
                (miro[ni][nj] != 1) and 
                (not visited2[ni][nj])):
                if DFS2(ni,nj):
                    return 1
        # for 문을 다 돌았는데도 못찾았다면
        else:
            return 0
 
for testcase in range(1, T+1):
    # 미로(배열)의 크기
    N = int(input())
    # 미로
    miro = [list(map(int, input())) for _ in range(N)]

    # 재귀 호출 용 방문 배열
    visited2 = [[0] * N for _ in range(N)]

    # 탐색 시작 좌표
    # si, sj
    for i in range(N):
        for j in range(N):
            if miro[i][j] == 2:
                # 시작점
                si, sj = i, j
    
    print(f"#{testcase} {DFS(si, sj)}")