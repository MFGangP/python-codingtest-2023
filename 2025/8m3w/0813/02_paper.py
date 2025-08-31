import sys
sys.stdin = open("paper_input.txt", mode='r')
sys.stdout = open("paper_output.txt", mode='w') 

def dp(n):
    if n == 10:
        return 1
    if n == 20:
        return 3

    return dp(n - 10) + 2 * dp(n - 20)

T = int(input())

for testcase in range(1, T+1):
    N = int(input())

    result = dp(N)
    print(f"#{testcase} {result}")
