# 2
# ()(((()())(())()))(())
# (((()(()()))(())()))(()())
import sys
sys.stdin = open("pipe_input.txt", "r")
sys.stdout = open("pipe_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):

    array = list(input())

    lazer_array = []
    pipe_array = []

    for i in range(len(array)):
        