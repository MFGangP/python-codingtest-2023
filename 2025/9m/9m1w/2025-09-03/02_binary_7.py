bit = "0000000111100000011000000111100110000011000011111001110011111001100111"

# 이진수를 7칸씩 쪼개서 십진수로 만들기
N = len(bit)

# 내장 함수가 "있긴 하다."" 직접 구현하는 방법을 연습하자
def binary_to_decimal(binary_str):
    len_binary_sty = len(binary_str)
    if len_binary_sty == 1:
        return int(binary_str[0]) * (2**(len_binary_sty-1))
    decimal_val = int(binary_str[0]) * (2**(len_binary_sty-1))
    another_val = binary_str[1:]
    return (decimal_val + binary_to_decimal(another_val))

# 길이가 14니까
# 0번 ~ 6번 잘라서 바꾸고
# 7번 ~ 13번 잘라서 바꾸고
for i in range(0, N, 7):
    # i번 비트에서 7칸 잘라서 십진수로 만들고 출력
    ith_bin = bit[i:i+7]

    # 십진수로 바꾸기
    decimal = binary_to_decimal(ith_bin)

    print(f"#{i}번 idx 슬라이싱 : {decimal}")