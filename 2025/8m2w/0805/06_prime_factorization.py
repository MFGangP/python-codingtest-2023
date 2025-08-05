T = int(input())

def prime_factorization(num):
    division11 = division7 = division5 = division3 = division2 = 0

    while num > 1:
        if num % 2 == 0:
            division2 += 1
            num = num // 2
        if num % 3 == 0:
            division3 += 1
            num = num // 3
        if num % 5 == 0:
            division5 += 1
            num = num // 5
        if num % 7 == 0:
            division7 += 1
            num = num // 7
        if num % 11 == 0:
            division11 += 1
            num = num // 11

    return print(f"#{time} {division2} {division3} {division5} {division7} {division11}")

for time in range(1, T+1):
    num = int(input())
    prime_factorization(num)

