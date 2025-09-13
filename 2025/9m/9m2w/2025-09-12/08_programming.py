
import sys
from collections import deque
sys.stdin = open("programming_input.txt", "r")
sys.stdout = open("programming_output.txt", "w")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def exe():
    # 처음 위치 (0,0)
    r = c = 0
    # 처음 방향 : 오른쪽
    d = 3
    # 처음 메모리 값 : 0
    m = 0
    # v: (r,c) 위치에서 메모리 값 m 일때, 방향 d일때 방문 체크
    v = set()

    # ? 때문에 큐에 넣고 처리
    q = deque([(r, c, d, m)])

    while q:
        # row, col, direction, memory
        r, c, d, m = q.popleft()

        # 현재 위치 처리한적 있으면 넘어가
        # 종료하면 안되는 이유는
        # 아직 가능성이 남아있는 노드가 큐 안에 있을수도..
        if (r, c, d, m) in v:
            continue

        # 현재 위치 처리 완료
        v.add((r, c, d, m))

        # for i in range(R):
        #     for j in range(C):
        #         if (i,j) == (r,c):
        #             print("*", end="")
        #         else:
        #             print(program[i][j],end="")
        #     print()
        #
        # print(d,m)

        # 현재 위치 값에 따라 명령 실행
        if program[r][c] == "@":  # 종료
            return "YES"
        elif program[r][c] in "^v<>":  # 방향 변경
            d = "^v<>".index(program[r][c])
        elif program[r][c] == "_":  # 0 아님 좌 0이면 우
            if m:
                d = 2
            else:
                d = 3
        elif program[r][c] == "|":  # 0 아님 상 0이면 하
            if m:
                d = 0
            else:
                d = 1
        elif program[r][c].isdigit():  # 메모리에 저장
            m = int(program[r][c])
        elif program[r][c] == "+":  # 메모리 값 + 1
            m = (m + 1) % 16
        elif program[r][c] == "-":  # 메모리 값 - 1
            m = 15 if m - 1 < 0 else m - 1
        elif program[r][c] == "?":  # 상하좌우 무작위
            # 상하좌우로 BFS
            for nd in range(4):
                q.append((r, c, nd, m))
        # . 은 아무것도 안해도됨

        # 이동
        r += dr[d]
        r = r % R

        c += dc[d]
        c = c % C

        q.append((r, c, d, m))
    
    # 큐 다 돌았는데 @ 못만나면 프로그램 종료 못함
    return "NO"


T = int(input())
for tc in range(1, T + 1):
    R, C = map(int, input().split())

    program = [list(input()) for _ in range(R)]

    print(f"#{tc} {exe()}")