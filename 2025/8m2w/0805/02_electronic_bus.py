# 노선 수
# ( 1 ≤ T ≤ 50 )
T = int(input())
 
for time in range(1, T + 1):
    # 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다.
    # ( 1 ≤ K, N, M ≤ 100 ) 정류장 번호 범위
    # K = 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
    # N = 종점인 N번 정류장
    # M = 충전기가 설치된 M개의 정류장
    K, N, M = map(int, input().split())
    # 충전기가 설치 된 정류장 번호를 입력으로 받는다
    electronic_bus_stop = list(map(int, input().split()))
    # 버스 현재 에너지
    # 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
    bus_energy = K
    # 버스 충전 횟수
    charge_time = 0
    # N 개 만큼 인덱스를 가진 빈 리스트 생성
    COUNTS = [0] * (N + 1)
    # 빈 정류장 계산
    empty_charge_station = 0
    # 정류장 계산
    for i in range(len(electronic_bus_stop)):
        # 충전기가 설치된 버스 정류장 번호대로 + 1
        COUNTS[electronic_bus_stop[i]] += 1
    # 배열 검색 했을 때 주유가 불가능한 상황 나오면 종료
    for i in range(len(COUNTS)):
        if empty_charge_station >= K:
            break
        elif COUNTS[i] == 0:
            empty_charge_station += 1
        else:
            empty_charge_station = 0
 
    # 그러면 여기서 [1 3 5 7 9] 일 때
    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]처럼 생길 것
    # 최종 목적지인 정류장 갯수만큼 반복
    if empty_charge_station >= K:
        # 0을 리턴하고 반복 문 자체 종료
        print(f"#{time} {0}")
        continue
    for i in range(N-(K-1)):
        # [3 10 5] k = 3 , n = 10
        # k - 한번에 갈 수 있는 거리
        # n - 충전기 설치된 정류장 수
 
        # 연료 소비했을 때
        if bus_energy != K:
            # 남은 에너지 값 만큼 반복
            for energy in range(bus_energy + 1):
                # 내 에너지로 갈 수 있는 앞선 정류장에 주유소가 있다면
                if COUNTS[i + energy] == 1:
                    # 지금 가진 연료로 갈 수 없는 거리일 때
                    if i - energy >= bus_energy:
                        # 지금 밟고 있는 곳이 충전소이면
                        if COUNTS[i] == 1:
                            # 에너지 충전
                            bus_energy = K
                            charge_time += 1
                            break
                    # 지금 연료로 갈 수 있으면
                    else:
                        # 충분하면 진행1
                        bus_energy -= 1
                        break
        # 연료 최대치 일때
        else:
            bus_energy -= 1
            continue
    print(f"#{time} {charge_time}")