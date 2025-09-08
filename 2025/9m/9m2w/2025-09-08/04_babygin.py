import sys
sys.stdin = open("babygin_input.txt", "r")
sys.stdout = open("babygin_output.txt", "w")

# 탐욕 알고리즘을 써서 풀어봐라
# 카드가 몇장 있는지 체크해서 트리플인지 런인지 확인하는 방식으로
# 카운팅 배열 쓰면 될 듯.
T = int(int(input()))

def check_babygin(player_cards, player_num):
    for i in range(10):
        # 숫자 i 카드를 보고
        # 숫자 i 카드가 3장 이상 => triple
        if player_cards[i] >= 3:
            return player_num
        # 숫자 i 카드, i+1 카드, i+2카드 3장 다 1장 이상씩 있다면 => run
        elif i < 8 and player_cards[i] > 0 and player_cards[i+1] > 0 and player_cards[i+2] > 0:
            return player_num

for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player_1_cards = [0] * 10
    player_2_cards = [0] * 10

    result = 0

    for i in range(len(cards)):
        # 인덱스라서 짝수 홀수 신경써야함.
        # 홀수번 카드를 받는 경우
        if i % 2 == 0:
            # i번 카드의 등장 횟수를 1 증가
            player_1_cards[cards[i]] += 1
            # 카드를 받았으면 babygin 해당 여부 판별
            result = check_babygin(player_1_cards, 1)
            if result:
                print(f"#{tc} {result}")
                break
        # 홀수번 카드를 받는 경우
        else:
            player_2_cards[cards[i]] += 1
            # 카드를 받았으면 babygin 해당 여부 판별
            result = check_babygin(player_2_cards, 2)
            if result:
                print(f"#{tc} {result}")
                break
    else:
        print(f"#{tc} 0")
        
