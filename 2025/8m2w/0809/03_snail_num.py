import sys

sys.stdin = open("kill_fly_input.txt", mode='r')
sys.stdout = open("kill_fly_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):

    N = int(input())

    for i in range(N):
        for j in range(N):
            pass