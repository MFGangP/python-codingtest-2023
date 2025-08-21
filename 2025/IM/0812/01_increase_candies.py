import sys
sys.stdin = open("increase_candies_input.txt", mode='r')
sys.stdout = open("increase_candies_output.txt", mode='w') 
# 그리디(Greedy) 알고리즘
# 탐욕 탐색
def eat_candies(candies):
    eat_times = 0
    # 상자는 최소 1, 2, 3개의 사탕이 있어야한다.
    if candies[2] < 3 or candies[1] < 2 or candies[0] < 1:
        return -1
    else:
        while candies[1] >= candies[2]:
            candies[1] -= 1
            eat_times += 1
        while candies[0] >= candies[1]:
            candies[0] -= 1
            eat_times += 1
        return eat_times
    
T = int(input())

for testcase in range(1, T+1):
    candies = list(map(int, input().split()))
    eat_time = eat_candies(candies)
    print(f"#{testcase} {eat_time}")