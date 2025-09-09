import sys

sys.stdin = open("telephone_pole_input.txt", "r")
sys.stdout = open("telephone_pole_output.txt", "w")

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    # N 개의 새로운 선이 추가 (기존 선들과 비교)
    # 기존 선들을 저장할 리스트
    wires = []
    # 교차점 수
    answer_count = 0 

    for _ in range(N):
        start, end = map(int, input().split())

        # 기존 선들과 비교
        for prev_start, prev_end in wires:
            # 1. 기존의 전선보다 시작점이 높고, 도착점이 낮음
            if start > prev_start and end < prev_end:
                answer_count += 1
            # 2. 기존의 전선보다 시작점이 낮고, 도착점이 높음
            if start < prev_start and end > prev_end:
                answer_count += 1

        # 목록에 추가
        wires.append((start, end))

    print(f"#{tc} {len(answer_count)}")