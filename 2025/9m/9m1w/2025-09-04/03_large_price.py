import sys
sys.stdin = open("large_price_input.txt", "r")
sys.stdout = open("large_price_output.txt", "w")

# 교환 횟수(k)를 단계로 표현해보자
def solve(k):
    global max_price
    # 가지 치기
    # k 번 교환해서 만든 문자열을 이전에 만든적이 있다면:
    current_state = "".join(numbers)
    if (k, current_state) in check:
        return
    # 현재 상태를 기록
    check.add((k, current_state)) 

    # 종료
    if k == cnt:
        int_numbers = int("".join(numbers))
        # 만든 숫자가 최대값인가? 비교해서 갱신
        if max_price < int_numbers:
            max_price = int_numbers
        return
    
    # 재귀 호출 진입 (다음단계)
    # 자리를 교환해서 다음 단계(다음 교환횟수)
    # 자리를 교환할 반복문 두개가 필요하고
    # 앞쪽자리 인덱스 i : 0 ~ N-2, 
    # 뒷쪽자리 인덱스 j : i+1 ~ N-1
    for i in range(N-1):
        for j in range(i+1, N):
            # 자리 교환
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 재귀 호출
            solve(k + 1)
            # 원래대로 되돌려 놓기 (백트래킹)
            numbers[i], numbers[j] = numbers[j], numbers[i]

    # i와 j를 정해서 자리 바꾸기
    # 자리 바꾼 다음에 다음 교환 횟수로 => 재귀 호출, 교환 횟수+1
    # 바꾼 자리 값을 구하고 난 뒤에
    # i와 j를 바꿔서 원상 복구

T = int(input())

for tc in range(1, T+1):
    # numbers : 처음 숫자
    numbers, cnt = input().split()
    # 교환횟수
    cnt = int(cnt)
    # 카드가 몇개 있는지 확인 - 인덱스 확인용
    N = len(numbers)
    # 최대값 구하기 위한 변수
    max_price = 0
    # 중복 체크를 위한 세트 - 안에는 (교환횟수 k, k번 교환해서 만든 숫자열) 튜플로 저장
    # 3번의 교환을 통해서 "12345" 라는 숫자열을 이전에 만든 적이 있다면
    # 나중에 교환 순서는 다르지만 3번 교환을 통해 "12345"를 만들면
    # 여기서 다시 만드는 모든 숫자열은 중복이 된다.
    # 모든 자리에서 중복 교환을 허용하기 때문이다.
    check = set()

    numbers = list(numbers)
    # 교환 안했으니 교환 횟수 0부터 시작
    solve(0)

    print(f"#{tc} {max_price}")