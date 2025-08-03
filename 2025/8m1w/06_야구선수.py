# N명의 야구 선수가 있고, 각 선수는 특정한 실력을 가지고 있다.

# 이 야구선수들은 팀을 정해야 하는데 팀을 정할때 규칙이 존재한다.

# 팀을 정할때 규칙은 정해진 팀원 사이의 야구 실력의 차이가 최대 K를 넘지 않아야 한다는 것이다.

# 야구 선수들의 실력 정보가 주어졌을때, 팀의 인원이 최대한 많게 구성하고 싶다.
# 최대가 되도록 구성했을때, 몇명이 되는지 구하는 프로그램을 작성하시오.

# 맨 첫줄에 테스트케이스의 개수가 주어진다.
# 각 테스트케이스마다 첫 줄에 야구선수 인원 N, 허용가능한 실력 K가 주어지고.
# 두 번째 줄에 N명의 야구선수들의 실력이 입력으로 주어진다.

# 예제)
# 야구 선수들의 실력이 각각 아래와 같을때, 허용 가능한 실력 차이가 3이면
# 1 2 3 4
# 1 2 3 4 모든 야구 선수가 한 팀에 들어가면 실력이 제일 낮은 선수는 실력이 1, 실력이 가장 높은 선수는 실력이 4 이기 때문에
# 최대 실력 차이가 3이 된다. 그래서 모든 팀원과 팀 구성이 가능하므로 최대 팀원은 4명이 된다.

# 3
# 4 2
# 6 4 2 3
# 4 3
# 1 2 3 4
# 4 1
# 1 3 7 5

#1 3
#2 4
#3 1

# 총 계산 횟수
T = int(input())

for time in range(1, T+1):
    baseball_player_numbers, skill_gap = map(int, input().split())
    baseball_players = sorted(list(map(int, input().split())))

    total_gap_in_player = 0
    left = 0
    # 슬라이딩 윈도우 기법
    # 오른쪽 포인터가 계속 증가하면서 왼쪽 포인터랑 값 비교를 함
    for right in range(baseball_player_numbers):
        # right 2 -> 3 -> 4 -> 6
        # left  2 -> 2 -> 2 -> while문
        # while에서 능력치 최대 허용치 아래로 내려올 때까지 left 포인터를 right로 당김
        while baseball_players[right] - baseball_players[left] > skill_gap:
            left += 1
        # 두 값을 비교해서 더 큰 값을 총 값에 대입
        total_gap_in_player = max(total_gap_in_player, right - left + 1)
    print(f"#{time}", total_gap_in_player)