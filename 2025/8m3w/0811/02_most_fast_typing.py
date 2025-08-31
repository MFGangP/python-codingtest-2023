# 일일이 타이핑 하는 것이 아닌 키를 눌려서 한번에 타이핑이 가능
# A = 전체 단어, B = 부분 단어
# 몇번 타이핑 해야 완성할 수 있는지 회수의 최솟값을 구해라
import sys
sys.stdin = open("most_fast_typing_input.txt", mode='r')
sys.stdout = open("most_fast_typing_output.txt", mode='w')

T = int(input())

for time in range(1, T+1):
    # A는 전체 단어, B는 부분 단어
    A, B = list(input().split())

    word_times = 0
    i = 0
    # A 길이만큼 반복하면서 B가 들어있는지 확인
    while len(A) > i :
        # A 내부에 B와 동일한 str이 있다면
        if A[i:i+len(B)] == B:
            word_times += 1
            i += len(B)
        else:
            word_times += 1
            i += 1
            
    print(f"#{time} {word_times}")
            