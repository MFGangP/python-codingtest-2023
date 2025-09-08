T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    time, sum_index = map(int, input().split())
    list_int = list(map(int, input().split()))
    sum_value = min_value = max_value = 0

    # sum_index개씩 더해보면서 최저 최대 값 갱신 해 줘야함.
    for i in range(len(list_int)):
        if i < sum_index:
            sum_value += list_int[i]
            min_value = max_value = sum_value
            # i 에 sum_index 를 뺀
            # 리스트를 빼주고 현재 리스트를
            # 더해주면 될거 같음
        elif i >= sum_index:
            sum_value -= list_int[i - sum_index]
            sum_value += list_int[i]
            if min_value > sum_value:
                min_value = sum_value
            if max_value < sum_value:
                max_value = sum_value
    print(f"#{test_case} {(max_value-min_value)}")
