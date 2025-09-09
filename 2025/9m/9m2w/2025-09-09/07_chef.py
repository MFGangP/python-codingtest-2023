import sys
sys.stdin = open("chef_input.txt", "r")
sys.stdout = open("chef_output.txt", "w")

T = int(input())

def calculate_synergy(team):
    synergy = 0
    # 팀 사이즈 만큼 원소를 가지고 있음.
    team_size = len(team)
    # 0번 인덱스부터 차례대로 쌍 만들기
    for i in range(team_size):
        for j in range(i+1, team_size):
            p1 = team[i]
            p2 = team[j]
            # 두 재료 순서에 따른 시너지의 합
            synergy += S[p1][p2] + S[p2][p1]
    return synergy

def dfs(index, team_A):
    global result

    # team_A가 재료 선택을 마쳤을 경우
    if len(team_A) == N//2:
        # team_B는 team_A에 들어있지 않은 재료로 구성
        team_B = [i for i in range(N) if i not in team_A]
        # N//2개의 재료로 가능한 시너지 계산하기
        synerge_A = calculate_synergy(team_A)
        synerge_B = calculate_synergy(team_B)
        # 두 시너지의 차
        diff = abs(synerge_A - synerge_B)
        # 최소 값 갱신
        result = min(result, diff)

    # 모든 재료를 확인했는데 실패했을 경우
    if index == N:
        return 
    
    # 다음 재료 찾기 위해 재귀
    # 현재 재료 넣고 재귀
    dfs(index+1, team_A+[index])
    # 현재 재료 넣지 않고 재귀
    dfs(index+1, team_A)

for tc in range(1, T+1):
    # N 개의 재료
    N = int(input())
    # 재료 시너지 표
    S = [list(map(int, input().split())) for _ in range(N)]
    # 최소 값을 담을 변수
    result = float("inf")
    
    dfs(0, [])

    print(f"#{tc} {result}")