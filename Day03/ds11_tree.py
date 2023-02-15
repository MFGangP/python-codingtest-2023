class TreeNode: # 트리 노드

    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None

memory = []

root = None
nameArry = ['블랙핑크', '레드밸벳', '마마무', '에이핑크', '걸스데이', '트와이스']

node = TreeNode()
node.data = nameArry[0]
root = node
memory.append(node)

for name in nameArry[1:]:

    node = TreeNode()
    node.data = name

    current = root
    while True:
        if name < current.data: # 부모노드 왼쪽
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:                   # 부모노드 오른쪽
            if current.right == None :
                current.right = node
                break
            current = current.right 
        
    memory.append(node) # 메모리에 저장

print('이진 탐색 트리 구성 완료')

print('--------------------------------------')

print('       ',root.data) # 루트(레벨0) 화사   
print('      ↙           ↘') # 분배
print('  ',root.left.data, end='     ') # 레벨1 솔라
print(root.right.data) # 레벨1  문별
print('  ↙        ↘           ↘') # 분배
print(root.left.left.data, end='  ') # 레벨2 휘인 
print(root.left.right.data, end='      ') # 레벨2 쯔위
print(root.right.right.data) # 레벨2 사나

print('--------------------------------------')

findName = str(input('찾을 이름을 입력해주세요 : '))

current = root
while True:
    if findName == current.data:
        print(findName,'를 찾았습니다.')
        break
    elif findName < current.data: # 작으니까 왼쪽으로
        if current.left == None:
            print(findName,'를 못찾았습니다.')
            break
        current = current.left
    else:   # 오른쪽 노드로
        if current.right == None:
            print(findName,'를 못찾았습니다.')
            break
        current = current.right       
        
