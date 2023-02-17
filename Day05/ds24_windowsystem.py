# C:/Window/System32 파일 출력
import os

def makeFileList(folder):
    fnameAry = []   # 파일 이름 리스트
    folderName = 'C:/Windows/System32'  # 찾을 폴더 위치

    for _, _, fnames in os.walk(folderName): # 파일 이름 받아오기 반복
        for fname in fnames:
            fnameAry.append(fname)
    
    return fnameAry

def insertionSort(ary):
    n = len(ary) # n에 길이 저장
    for end in range(1, n): # 인덱스 1번부터 비교 시작
        for cur in range(end,0,-1): # 0번이랑 1번 비교해서 자리 교환 시작
            if ary[cur-1] < ary[cur]:   # 내림차순(역순정렬)
                ary[cur-1], ary[cur] = ary[cur], ary[cur-1] # 자리 변경

    return ary

fileAry = makeFileList('C:/Program Files/Common Files') # 파일 이름 받아오기
fileAry = insertionSort(fileAry) # 넣어서 정렬
print('파일명 역순 -->', fileAry) # 출력
