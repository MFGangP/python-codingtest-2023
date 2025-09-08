import sys
sys.stdin = open("tournament_input.txt","r")
sys.stdout = open("tournament_output.txt","w")

# 테스트 케이스 개수
T = int(input())

# 승자 찾기 - 인덱스를 받아야한다.
def find_winner(idx1, idx2):
    # 두 플레이어의 카드 값을 가져옴
    card1 = Cards[idx1]
    card2 = Cards[idx2]

    if card1 == card2:
        return idx1 # 무승부: 번호가 작은 쪽이 승자
    elif (card1 == 1 and card2 == 3) or \
         (card1 == 2 and card2 == 1) or \
         (card1 == 3 and card2 == 2):
        return idx1 # 첫 번째 플레이어 승
    else:
        return idx2 # 두 번째 플레이어 승

def tournament(start, end):
    # 한 명만 남았을 때
    if start == end:
        return start

    # 그룹을 두 개로 나눔.
    middle = (start + end) // 2
    
    # 그룹 별 재귀 함수 실행
    Group_A = tournament(start, middle)
    Group_B = tournament(middle + 1, end)
    
    # 최종 우승자 반환.
    return find_winner(Group_A, Group_B)


for testcase in range(1, T+1):
    # 인원 수
    N = int(input())
    # 카드 숫자 리스트 - 번호순
    Cards = list(map(int, input().split()))
    
    # 0부터 N-1까지의 인덱스로 토너먼트를 시작합니다.
    result_idx = tournament(0, N - 1)
    
    # 최종 결과에 +1을 해서 원래의 1번부터의 번호로 출력.
    print(f"#{testcase} {result_idx + 1}")