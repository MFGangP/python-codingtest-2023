import sys

sys.stdin = open("village_count_input.txt", "r")
sys.stdout = open("village_count_output.txt", "w")

T = int(input())

def make_set(x, y):
    p[y] = x

def find_set(x):
    # 자기 자신이 대표가 아니라면
    if p[x] != x:
        p[x] = find_set(p[x])
    # 자기 자신이 대표면 반환
    return p[x]

def union(y, x):
    king_y = find_set(y)
    king_x = find_set(x)

    if king_x != king_y:
        # rank를 기준으로 합침
        if rank[king_x] > rank[king_y]:
            p[king_y] = king_x
        else:
            p[king_x] = king_y
            # 만약 rank가 같다면, 한쪽의 rank를 1 증가
            if rank[king_x] == rank[king_y]:
                rank[king_y] += 1

for tc in range(1, T+1):
    # N : 출석 번호 개수
    # M : 신청서 개수
    N, M = map(int, input().split())

    p = [i for i in range(N + 1)] 
    rank = [0] * (N + 1) 

    for _ in range(M):
        x, y = map(int, input().split())
        union(y, x)

        # 팀 개수
    village_count = 0
    
    for i in range(1, N + 1):
        if p[i] == i:
            village_count += 1

    print(f"#{tc} {village_count}")