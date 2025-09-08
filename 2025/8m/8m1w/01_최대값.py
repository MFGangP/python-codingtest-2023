T = int(input())
for test_case in range(1, T + 1):
    Ti = int(input())
    numbers = list(map(int, input().split()))

    test_result = numbers[0]
    test_result_index = 0
   
    for i in range(0, Ti):
        if test_result <= numbers[i]:
            test_result = numbers[i]
    print(f"#{test_case}", test_result)
    
