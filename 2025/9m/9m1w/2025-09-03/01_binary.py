def decimal_to_binary(n):
    if n < 2:
        return str(n)
    division_val = str(n%2)
    another_val = decimal_to_binary(n//2)
    return another_val + division_val

binary_value = decimal_to_binary(19)
print(binary_value)

def decimal_to_hexadecimal(n):
    if n == 0:
        return 0
    
# 내장 함수가 "있긴 하다."" 직접 구현하는 방법을 연습하자
def binary_to_decimal(binary_str):
    if len(binary_str) == 1:
        return int(binary_str[0]) * (2**(len(binary_str)-1))
    decimal_val = int(binary_str[0]) * (2**(len(binary_str)-1))
    another_val = binary_str[1:]
    return (decimal_val + binary_to_decimal(another_val))

decimal_value = binary_to_decimal("10011")
print(decimal_value)