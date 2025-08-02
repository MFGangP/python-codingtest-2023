T = int(input())

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    Ti = int(input())
    numbers = list(map(int, input().split()))

    test_result = 0
    # ///////////////////////////////////////////////////////////////////////////////////
    for i in range(0, Ti):
        if test_result < numbers[i]:
            test_result = numbers[i]
    print(f"#{test_case}", test_result)
    # ///////////////////////////////////////////////////////////////////////////////////
