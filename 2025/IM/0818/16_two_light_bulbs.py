import sys
sys.stdin = open("two_light_bulbs_input.txt", "r")
sys.stdout = open("two_light_bulbs_output.txt", "w")

T = int(input())

for testcase in range(1, T+1):
    A, B, C, D = map(int, input().split())

    array = [0 for _ in range(101)]

    two_light_bulbs = 0
    # A초에 시작해서 B 초에 끝난걸 카운팅 배열에 추가
    for i in range(A, B):
        array[i] += 1
    # C초에 시작해서 D 초에 끝난걸 카운팅 배열에 추가
    for j in range(C, D):
        array[j] += 1

    for x in range(len(array)):
        # 전구 켜져있는 시간이 2시간 이상이면
        if array[x] >= 2: 
            two_light_bulbs += 1
        
    print(f"#{testcase} {two_light_bulbs}")