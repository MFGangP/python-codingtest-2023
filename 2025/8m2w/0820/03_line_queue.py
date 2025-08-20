# 파이썬의 리스트 메서드를 사용해서 큐 만들기

# 큐로 사용할 빈 리스트
q = []

for i in range(1, 4):
    q.append(i)

print(q)

# 원소 삭제하기
for i in range(3):
    # 이건 큐의 크기가 커질거 같다 이러면 쓰면 안된다.
    print(q.pop(0), end=', ')
print()

print(q)