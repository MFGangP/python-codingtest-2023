from collections import deque
import sys
sys.stdin = open("repeat_input.txt", "r")
sys.stdout = open("repeat_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    texts = list(input())

    que = deque()

    max_cnt = 0

    for text in texts:
        # 큐가 비어있지않다고 큐의 끝 값이 텍스트와 같다면
        if que and que[-1] == text:
            # 만약 큐 값과 리스트 내부 값이 같다면
            # 큐 값 꺼내기
            p_que = que.pop()
        else:
            que.append(text)
        
    max_cnt = len(que)

    print(f"#{testcase} {max_cnt}")