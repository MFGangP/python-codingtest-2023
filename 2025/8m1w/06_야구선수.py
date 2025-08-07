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