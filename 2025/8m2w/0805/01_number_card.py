# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )

# 케이스 개수 T
T = int(input())

for time in range(T):
    # 카드 장수 N
    N = int(input())
    # 데이터
    card_numbers = list(map(int, input()))
    # N개의 숫자 ai가 여백없이 주어진다.(0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 )
    COUNTS = [0] * 10
    # 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤,
    # 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

    # 가장 많은 카드의 숫자 = 첫번째 카드 등록
    max_num = card_numbers[0]
    # 가장 많은 카드 장수
    max_count = 0
    # 카드의 개수 만큼 돌면서 카드 갯수 카운팅
    for i in range(N):
        COUNTS[card_numbers[i]] += 1
    # 중간에 0을 가진 칸이 많이 생긴다
    for i in range(len(COUNTS)):
        # 정렬된 리스트 안에 값이 있다면
        if COUNTS[i] > 0:
            # 최대 갯수 max_count(이전 최대값)가 COUNTS[i](갱신할 값)보다 작거나 같고,
            # 최고 값이 i보다 작다면
            if max_count <= COUNTS[i] and max_num <= i:
                max_count = COUNTS[i]
                max_num = i

    print(f"#{time + 1} {max_num} {max_count}")
