import sys
sys.stdin = open("cargo_dock_input.txt", "r")
sys.stdout = open("cargo_dock_output.txt", "w")

T = int(input())

for tc in range(1, T + 1):
    # 화물 도크 이용 신청서 N개
    N = int(input())

    # (작업시작시간, 작업종료시간) 형태의 입력이 N줄
    # [[s1,e1], [s2,e2] , ... [sn, en]]
    time_table = [list(map(int, input().split())) for _ in range(N)]

    # 위에 있는 리스트를 끝나는 시간(e)를 기준으로
    # 끝나는 시간이 빠른 것이 앞으로 오도록 정렬
    # 끝나는 시간 기준 오름차순 정렬
    time_table.sort(key=lambda e: e[1])

    # 최대 작업의 개수
    count = 0

    # 작업 종료 시간이 빠른 것 부터 선택
    # 현재 작업의 시작 시간이 si라고 하면
    # 이전 작업의 끝나는 시간 ei-1 보다 현재 작업 시작 시간이 크거나 같아야한다.
   
    # 이전 작업 끝난 시간
    last_end_time = 0

    for i in range(N):
        # i번 작업의 시작 시간, 종료 시간
        start_time = time_table[i][0]
        end_time = time_table[i][1]

        # i번 작업은 이전 작업의 끝 시간 보다
        # i번 작업의 시작 시간이 크거나 같아야한다.
        if start_time >= last_end_time:
            # 이 작업을 고른다.
            count += 1
            # 이 작업이 끝나는 시간을 갱신
            last_end_time = end_time
        
    print(f"#{tc} {count}")

