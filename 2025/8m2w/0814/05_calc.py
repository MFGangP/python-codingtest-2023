import sys
sys.stdin = open("calc_input.txt", mode='r')
sys.stdout = open("calc_output.txt", mode='w') 

for testcase in range(1, 11):
    # 테스트 케이스 길이
    Test_len = int(input())

    #테스트 케이스
    Test_case = list(map(input()))

    