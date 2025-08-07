T = int(input())
for test_case in range(1, T + 1):
    time = int(input())
    list_int = list(map(int, input().split()))
    for i in range(time-1):
        for j in range(time-1):
            if list_int[j] > list_int[j+1]:
                list_int[j], list_int[j+1] = list_int[j+1], list_int[j]
    print(f"#{test_case}",list_int[time-1] - list_int[0])