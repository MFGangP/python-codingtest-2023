import sys
sys.stdin = open("carrot_input.txt", mode='r')
sys.stdout = open("carrot_output.txt", mode='w') 

T = int(input())

small = []
middle = []
big = []

def count_carrot(carrot_count_dict: dict):
    is_posible = False

    if is_posible:
        # 포장 횟수 리턴
        return 0
    else:
        return -1

for testcase in range(1, T+1):
    # 당근 갯수
    N = int(input())
    # 당근 크기
    Ci = list(map(int, input().split()))

    carrot_count_dict = {}

    for carrot in Ci:
        carrot_count_dict[carrot] = carrot_count_dict.get(carrot, 0) + 1
    
    result = count_carrot(carrot_count_dict)

    print(f"#{testcase} {result}")