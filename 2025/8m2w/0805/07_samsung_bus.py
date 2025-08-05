T = int(input())
# N
# 첫번째 테스트 케이스 입력 갯수
# P
# 두번째로 들어오는 하나의 정수 갯수
N = P = 0

# 정확히 버스 노선이 동일한 번호 개수
for time in range(1, T+1):
    correct_match_numbers = []
    bus_stops = []
    bus_numbers = []

    N = int(input())
    for _ in range(N):
        # i번째 버스 노선은 번호가 bus_numbers[x][0]이상
        # bus_numbers[x][1]이하인 모든 정류장을 다니는 버스 노선
        bus_number = list(map(int, input().split()))
        bus_numbers.append(bus_number)
    # P개의 버스 정류장 번호를 입력받는다.
    P = int(input())
    for _ in range(P):
        # 입력받은 정류장 번호 P개를 bus_stops에 받는다.
        bus_stop = int(input())
        bus_stops.append(bus_stop)

    # 숫자별로 갯수를 늘려줘야한다.
    bus_stop_counts = [0] * 5001

    # N에서 받은 숫자 쌍의 개수만큼 반복하면서
    # 입력받은 번호 A1~Ax, B1~Bx 까지 수 안에 존재하는 
    # bus_numbers 0번 인덱스에서 1번 인덱스까지의 숫자를 검색한다.

    # 버스 리스트 내에서 bus_num 갯수를 찾아야한다.
    for bus_number in bus_numbers:
        # bus_stops 내의 숫자 개수를 찾아내야한다.
        for stop_num in range(bus_number[0], bus_number[1] + 1):
            bus_stop_counts[stop_num] += 1
        # 같은 번호를 다 구했을 때 반환 리스트에 추가

    print(f"#{time} ", end='')
for i in range(len(bus_stops)):
    # 마지막 요소는 공백 없이 출력
    if i == len(bus_stops) - 1:
        print(bus_stop_counts[bus_stops[i]], end="")
    # 그 외는 공백 출력
    else:
        print(bus_stop_counts[bus_stops[i]], end=" ") 
        