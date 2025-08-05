# 노선 수
# ( 1 ≤ T ≤ 50 )
T = int(input())

def drive(K, N):
    # K : 한번 충전시 이동 가능한 정류장 개수
    # N : 마지막 도착 정류장 번호

    # return 값 == 0 : 버스가 마지막 정류장에 도착하지 못함
    # return 값 > 0 : 버스가 마지막 정류장에 도착함

    last = 0 # 마지막에 충전한 위치
    bus = K # 버스가 최대로 움직인 위치 (초기 값은 한번 최대로 이동)
    count = 0 # 충전 횟수, 시작 충전은 횟수 제외

    # 버스 위치가 N 보다 작으면 계속 움직여라
    while bus < N:
        # 현재 위치에 충전기가 있는지 확인
        # 충전기가 없으면 앞으로 가서 다시 확인
        while stop_list[bus] == 0:
            # 충전기가 없으면 되돌아와라
            bus -= 1
            # 마지막에 충전한 위치로 돌아와 버리면 운행 불가
            if bus == last:
                return 0
        # stop_list[bus] == 1 인곳을 만나면 반복 중단
        # 더 갈 수 있다는 것을 의미
        last = bus
        # 충전 했으니 충전 횟수 + 1
        count += 1
        # 충전했으니 K칸 쭉 땡기기
        bus += K
    # 반복이 종료되면 충전 횟수 return
    return count

for time in range(1, T + 1):
    # 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다.
    # ( 1 ≤ K, N, M ≤ 100 ) 정류장 번호 범위
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
    # N = 종점인 N번 정류장
    # M = 충전기가 설치된 M개의 정류장
    K, N, M = map(int, input().split())
    # 충전기가 설치 된 정류장 번호를 입력으로 받는다
    charger_list = list(map(int, input().split()))

    # 정류장 리스트
    stop_list = [0] * N
    # stop_list[1] == 1 = 충전기 있음
    # stop_list[2] == 0 = 충전기 없음

    # 충전기가 있는 정류장 번호를 확인
    for x in charger_list:
        # x번 정류장에는 충전기가 있다고 표시
        stop_list[x] = 1

    answer = drive(K,N)
    print(f"#{time} {answer}")

