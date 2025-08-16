import sys
sys.stdin = open("paper_input.txt", mode='r')
sys.stdout = open("paper_output.txt", mode='w') 

def dp(boxsize):

    pass

# 테스트 케이스는 50가지
for testcase in range(1, 51):
    # 10의 배수인 사각형 길이
    N = int(input())
    
    dp_array = [[0] for _ in range(301)]