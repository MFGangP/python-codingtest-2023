T = int(input())
max_time = 0
input_list = list(map(int, input().split()))
for i in range(T):
    temp = input_list[0]
    time_num = 0
    for j in range(T - 1):
        if input_list[j] > input_list[j + 1]:
            temp = input_list[j]
            input_list[j] = input_list[j + 1]
            input_list[j + 1] = temp
            time_num += 1
        if max_time < time_num:
            max_time = time_num
print(f"{max_time}")
