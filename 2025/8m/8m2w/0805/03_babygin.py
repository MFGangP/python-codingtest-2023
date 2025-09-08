T = int(input())

for time in range(1, T+1):
    num = int(input())

    # 숫자 카드의 개수를 세기 위한 카운팅 배열
    counts = [0] * 12 # 왜 10개가 아니라 12개인지는 아래 나옴.

    # 456789 => 45만 6789인데 우리가 원하는 건 각 자리수의 숫자
    # 우리가 사용하는 숫자의 진법은 10진법
    # 456789를 10으로 나눈 나머지 => 9, 9의 개수를 1증가
    # counts[9] += 1
    # 다음 나눌 수는 456789를 10으로 나눈 몫
    # 45678을 10으로 나눈 나머지 => 8, 8의 개수를 1 증가,
    # counts[8] += 1
    # 다음 나눌 수는 45678를 10으로 나눈 몫
    # ...
    # 4를 10으로 나눈 나머지 => 4....

    # 6번 반복
    for i in range(6):
        counts[num%10] += 1
        num //= 10

    # run인지 triplet인지 확인
    # run의 개수 => run_cnt
    # triplet의 개수 => tri_cnt
    run_cnt = tri_cnt = 0
    # 두 개수의 합이 2면 baby_gin 완성
    # 완성이 되는 조건 : run2/ tri2/ run1/ tri1

    # run 인지 triple 인지 확인을 하는데, 기준 숫자 번호 i
    i=0
    # 숫자 카드의 범위는 0 <= i < 10
    while i < 10:
        # 트리플 부터 확인
        # 숫자 i의 개수가 3이상 => 트리플 가능, 왜 3개 이상인가?
        if counts[i] >= 3:
            # 숫자 i로 트리플 만들었으니 i 개수 -3
            counts[i] -= 3
            # 트리플 개수 + 1
            tri_cnt += 1
            continue
        # 런확인
        # 숫자 i, i+1, i+2도 1개 이상 => 런 가능, 왜 1개 이상인가?
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1
            # 런 개수 +1
            run_cnt += 1
            continue
        # 트리플도 없고 런도 없었으면 다음 숫자 확인
        i += 1
    # 런 + 트리플 == 2 이면 Baby Gin
    if run_cnt + tri_cnt == 2:
        print(f"#{time} Baby Gin")
    else:
        print(f"#{time} Lose")