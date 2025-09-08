import sys
sys.stdin = open("binary_simple_password_input.txt", "r")
sys.stdout = open("binary_simple_password_output.txt", "w")


T = int(input())

code_table = {
    "0001101" : 0,
    "0011001" : 1,
    "0010011" : 2,
    "0111101" : 3,
    "0100011" : 4,
    "0110001" : 5,
    "0101111" : 6,
    "0111011" : 7,
    "0110111" : 8,
    "0001011" : 9,
}

result = 0

def find_code():
    global result

    # 코드 찾기
    for i in range(N):
        # j는 열 번호인데 뒤에서부터 1 찾기 시작
        # 왜 1을 찾느냐?? 모든 암호코드는 다 1로 끝난다
        # 0으로 시작하는 것도 당연하긴 한데 0이
        # 암호코드에 포함되는지 아닌지 확인
        for j in range(M-1, 55, -1):
            if matrix[i][j] == "1":
                # 암호코드가 끝나는 위치 j를 발견했으니까
                # [j-55 , j] 암호코드 후보 범위
                code = matrix[i][j-55: j+1]
                # 7개씩 짤라서 8개가 나오게 된다.
                # code를 앞에서 부터 7개씩 잘라서 code_table에 일치하는 
                # 코드가 있는지 확인하기
                # 여기 완성해보기
                # 짝
                nums = []
                for p in range(0, 50, 7):
                    nums.append(code_table.get(code[p:p+7]))
                odd = 0
                even = 0
                for idx in range(len(nums)):
                    # 인덱스 기준으로 짝홀 판명하는거라 나머지가 반대
                    if nums[idx] == None:
                        return print(f"#{tc} 0") 
                    elif idx % 2 == 1:
                        odd += nums[idx]
                    elif idx % 2 == 0:
                        even += nums[idx]
                result = even * 3 + odd
                if result % 10 == 0:
                    return print(f"#{tc} {odd + even}")
                else:
                    return print(f"#{tc} 0")  

for tc in range(1, T+1):
    # N : 세로크기
    # M : 가로크기
    N, M = map(int, input().split())

    # 1 또는 0으로 구성된 암호코드가 포함된 문자열 배열
    matrix = [input() for _ in range(N)]

    find_code()