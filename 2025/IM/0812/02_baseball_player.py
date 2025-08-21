import sys
sys.stdin = open("baseball_player_input.txt", mode='r')
sys.stdout = open("baseball_player_output.txt", mode='w') 

T = int(input())
# 슬라이딩 도어 기법
for testcase in range(1, T+1):
    # N 야구 선수 인원, 허용 가능한 실력 차이 K
    N, K = list(map(int, input().split()))
    # 야구 선수 리스트
    bs_players = list(map(int, input().split()))
    bs_players.sort()

    # 최대 플레이어 인원 수 
    number_of_player = 0
    start = 0

    # 실력 차이 사이 내의 최대 선수 풀을 만들어야 한다.
    for end in range(N):
        # 최대 최소의 차이가 허용가능 범위 밖이면
        while bs_players[end] - bs_players[start] > K:
            start += 1

        # 최대 최소의 차이가 허용가능 범위 안이면
        current_player = end - start +1
        if number_of_player < current_player:
                number_of_player = current_player

    print(f"#{testcase} {number_of_player}")