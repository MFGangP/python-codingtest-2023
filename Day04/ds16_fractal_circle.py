# 프랙탈 원 그리기
import turtle # 그림 그려주는 거북이
import tkinter as tk

t = turtle.Turtle()

c = t.clone()# 거북이 복제
c.color('red')
c.circle(30)

for i in range(4,10):
    c.circle(i * 10)

turtle.mainloop()