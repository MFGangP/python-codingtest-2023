A = [1, 2, 3, 4, 5]
B = [0] * 5

def mycopy(idx):
    if idx == 5:
        return B
    # B에 A값 넣어주기
    B[idx] = A[idx] 
    mycopy(idx+1)

mycopy(0)

print(*B)

A = [1, 2, 3, 4, 5]
B = 4

def search(idx):
    global check_bool
    if idx == 5:
        check_bool = False
        return check_bool
    elif A[idx] == B:
        check_bool = True
        return check_bool
    search(idx+1)

check_bool = False

search(0)
print(check_bool)