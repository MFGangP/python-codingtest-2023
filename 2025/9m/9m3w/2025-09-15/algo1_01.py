T = int(input())

for tc in range(1, T+1):
    # N : 정수의 개수
    # M : 윈도우 크기
    N, M = map(int, input().split())
    array = list(map(int, input().split()))
    # window 단위로 쪼개서 받을 리스트
    windows = []
    # 증가하는 윈도우 개수
    increased_window = 0
    # 단순증가패턴 확인 Bool 변수
    is_increased = False
    # N이 M의 배수인 경우
    if N % M == 0:
        windows_size = (N // M)
    # 배수가 아닌 경우
    else:
        # 윈도우 크기는 +1
        windows_size = (N // M) + 1

    for i in range(0, windows_size):
        windows.append(array[3*i:3*(i+1)])

    for window in windows:
        # 요소가 하나 있는 경우
        if len(window) == 1:
            increased_window += 1
            break
        # 요소가 M개보다 적은 경우
        elif len(window) <= M:
            for idx in range(len(window)-1):
                # 다음 요소가 증가하는 값이면
                if window[idx] < window[idx+1]:
                    is_increased = True
                # 다음 요소가 작거나 정체되어 있다면
                else:
                    # 다음 window 탐색
                    is_increased = False
                    break
            # window 확인이 끝났는데 단순 증가 패턴이면
            else:
                increased_window += 1

    print(f"#{tc} {increased_window}")