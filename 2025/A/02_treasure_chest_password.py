import sys
sys.stdin = open("treasure_chest_password_input.txt", "r")
sys.stdout = open("treasure_chest_password_output.txt", "w")

# 테스트 케이스 수
T = int(input())

for testcase in range(1, T + 1):
    N, K = map(int, input().split())
    data = list(input())
    
    side_len = N // 4
    passwords = set()
    
    # N/4번 회전하며 모든 경우의 수 탐색
    for _ in range(side_len):
        # 4개의 변에서 숫자를 추출하여 set에 추가 (자동으로 중복 제거)
        for i in range(4):
            # 각 변의 시작 인덱스
            start_idx = i * side_len
            # 각 변의 16진수 문자열
            password_str = "".join(data[start_idx : start_idx + side_len])
            # 10진수로 변환하여 set에 추가
            passwords.add(int(password_str, 16))
            
        # 뚜껑을 시계 방향으로 한 칸 회전
        # 마지막 요소를 맨 앞으로 이동
        last_char = data.pop()
        data.insert(0, last_char)
    
    # set을 리스트로 변환하고 내림차순 정렬
    sorted_passwords = sorted(list(passwords), reverse=True)
    
    # K번째로 큰 수 출력
    print(f"#{testcase} {sorted_passwords[K-1]}")