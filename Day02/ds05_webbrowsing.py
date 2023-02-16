# 스택 활용

import ds04_stack as st
import webbrowser   # 웹브라우저 모듈
import time         

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1

if __name__ == '__main__':
    urls = ['www.naver.com', 'www.google.com', 'www.daum.net', 'www.nate.com']

    for url in urls:
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url, end='-->')
        time.sleep(1)   # 1초 대기

    print('방문 종료')
    print(st.stack)
    time.sleep(5)   # 5초 대기

    while True:
        url = st.pop()
        if url == None:
            break
        else:
            webbrowser.open(f'https://{url}')
            print(url, end='-->')
            time.sleep(1)   # 1초 대기

    print('재방문 종료')
    print(st.stack)

    input('Wait : ')
