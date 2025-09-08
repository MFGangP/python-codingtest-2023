import sys
sys.stdin = open("babygin_game_input.txt", "r")
sys.stdout = open("babygin_game_output.txt", "w")

# 승리 여부를 판정하는 함수
def check_win(hand):
    # 카드가 3장 미만이면 판정 불가
    if len(hand) < 3:
        return False

    # 0~9 숫자 카드의 개수를 세는 배열
    counts = [0] * 10
    for card in hand:
        counts[card] += 1

    # Triplet 검사
    for count in counts:
        if count >= 3:
            return True

    # Run 검사
    for i in range(8): # 0~7까지만 확인 (i, i+1, i+2)
        if counts[i] > 0 and counts[i+1] > 0 and counts[i+2] > 0:
            return True
            
    return False


T = int(input())
for tc in range(1, T + 1):
    cards = list(map(int, input().split()))

    player1_hand = []
    player2_hand = []
    winner = 0
    
    # 받을 때마다 승리 여부 확인
    for i in range(12):
        # 플레이어 1이 이겼을 때
        if i % 2 == 0:
            player1_hand.append(cards[i])
            if check_win(player1_hand):
                winner = 1
                break
        # 플레이어 2가 이겼을 때
        else:
            player2_hand.append(cards[i])
            if check_win(player2_hand):
                winner = 2
                break

    print(f"#{tc} {winner}")