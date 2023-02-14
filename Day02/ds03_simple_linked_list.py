# 단순 연결 리스트 구현
# 노드 생성하는 클래스
class Node:
    def __init__(self):
        self.data = None
        self.link = None

# 전역 변수
memory = [] # list()
head, current, pre = None, None, None   # 변수 초기화
dataArray = ['다현', '정현', '쯔위', '사나', '지효']    # 리스트 선언

def printNode(start):   # 노드 보여주는 함수
    current = start
    if current == None:
        return
    print(current.data, end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print(current.data, end=' -> None')
        else:
            print(current.data, end=' -> ')

if __name__ == '__main__':
    node = Node() # 객체, 클래스 생성자
    # 노드를 빈 노드로 만든다.
    node.data = dataArray[0] # 다현
    # 노드 데이터에 다현을 삽입
    head = node  # head는 node 
    memory.append(node) # 메모리에 node 더하기

    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre = node
        node = Node()
        node.data = data    # 정연, 쯔위, 사나, 지효 순
        pre.link = node
        memory.append(node)

printNode(head) # 전체 출력