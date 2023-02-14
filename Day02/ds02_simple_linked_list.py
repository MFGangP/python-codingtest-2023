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

# 노드 추가

def insertNode(findData, insertData):
    global memory, pre, current, head 
    # 첫노드 앞에다 데이터를 넣겠다면
    if head.data == findData:   # 맨 앞의 데이터가 찾는 데이터라면
        node = Node() # 새로운 노드를 만들고
        node.data = insertData # 입력 받은 인서트 데이터를 노드 데이터에 삽입
        node.link = head   # 노드 링크를 헤드에 연결
        head = node # 맨 앞의 노드를 삽입한 노드로 변경
        # 결과적으로 기존의 헤드 데이터는 인서트 데이터로 변경된거고, 
        # 새로운 노드 데이터가 헤드 데이터가 된 것
        return

    current = head # current를 제일 앞으로
    # current 노드를 지금의 head 데이터로 덮어 쓰고
    while current.link != None: # current.link가 마지막이 아닐동안 
                                # 계속 돌면서 중간노드 추가
        pre = current # pre 노드를 current랑 똑같이 만들어주고
                      # 현재 current는 head 노드
        current = current.link # current노드는 하나 더 뒤로 가기
                               # 결과적으로 pre, current 

        if current.data == findData: # 만약에 current 데이터가 찾는 데이터면
            node = Node() # 새로운 노드를 만들어서
            node.data = insertData # 새 노드 데이터를 삽입 하려고 하는 데이터로 만들고
            node.link = current # 새 노드 링크는 current로 연결
            pre.link = node # pre와 current 중간에 새로 생성한 node가 들어감
            return
            # pre , node , current 순

    # current.link == None 까지 온 것
    node = Node()
    node.data = insertData
    current.link = node
    return

if __name__ == '__main__':
    node = Node() # 객체, 클래스 생성자
    # 빈 노드를 node라는 이름으로 만든다.
    node.data = dataArray[0] # 빈 노드에 dataArray[0]번인 다현 삽입
    head = node  # head를 새로 만든 노드 데이터랑 같게 만들기 
    memory.append(node) # 메모리에 새로만든 노드 더하기
    # head == node
    
    for data in dataArray[1:]: # 두번째 노드 이후 4번 반복
        pre = node  # pre가 '다현'을 가리킴
        node = Node()   # node를 새로운 노드로 바꿈
        node.data = data    # data 내부 값은 정연, 쯔위, 사나, 지효 순
        pre.link = node # pre 노드가 가르킬 다음 노드를 node로 지정
        memory.append(node) # 메모리에 node 추가

printNode(head) # 전체 출력