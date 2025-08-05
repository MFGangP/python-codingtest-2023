T = int(input())

for time in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input()))

    continue_one = 0
    max_continue_one = 0

    for i in range(N):
        if num_list[i] == 1:
            continue_one += 1
            if max_continue_one <= continue_one:
                max_continue_one = continue_one
        else:
            continue_one = 0
    print(f"#{time} {max_continue_one}")