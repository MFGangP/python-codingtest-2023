import sys
sys.stdin = open("check_in_out_input.txt", "r")
sys.stdout = open("check_in_out_output.txt", "w")

# 출입 기록 암호화
def check_in(id_list: list, check_list, N):
    for id in id_list:
        # 값이 이미 들어있는 id이면
        if check_list[id] == id:
            # check_list에 아이디에 해당하는 부분에 값 추가
            # 자기 자신을 두번 곱하면 0이 된다.
            check_list[id] ^= id 
        elif check_list[id] == 0:
            check_list[id] = id 
            
T = int(input())

for tc in range(1, T+1):
    # id 개수
    N = int(input())
    # 출입 기록 리스트
    id_list = list(map(int, input().split()))
    # 최종적으로 나가지않은 id 갯수
    in_bound_num = 0
    
    # 암호 등록할 체크 리스트
    check_list = [0 for _ in range(20001)]
    
    print(f"#{tc}", end="")

    # 출입 기록 암호화 후 동일 기록 체크
    check_in(id_list, check_list, N)

