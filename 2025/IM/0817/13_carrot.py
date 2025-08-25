import sys
sys.stdin = open("carrot_input.txt", mode='r')
sys.stdout = open("carrot_output.txt", mode='w') 

T = int(input())

for testcase in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))
    carrots.sort()

    # 그룹화
    groups = []
    count = 1
    for i in range(1, N):
        if carrots[i] == carrots[i-1]:
            count += 1
        else:
            groups.append(count)
            count = 1
    groups.append(count)  # 마지막 그룹 추가

    G = len(groups)
    answer = float('inf')

    # 그룹이 3개 미만이면 불가능
    if G < 3:
        print(f"#{testcase} -1")
        continue

    # prefix sum으로 빠른 계산
    prefix = [0] * (G+1)
    for i in range(G):
        prefix[i+1] = prefix[i] + groups[i]

    # cut 두 개 고르기
    for i in range(1, G-1):        # 첫 cut
        for j in range(i+1, G):    # 두 번째 cut
            small = prefix[i]
            middle = prefix[j] - prefix[i]
            big = prefix[G] - prefix[j]

            # 조건: 각 상자 최소 1개 이상
            if small > 0 and middle > 0 and big > 0:
                diff = max(small, middle, big) - min(small, middle, big)
                answer = min(answer, diff)

    if answer == float('inf'):
        print(f"#{testcase} -1")
    else:
        print(f"#{testcase} {answer}")