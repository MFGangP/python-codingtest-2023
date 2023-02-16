import turtle

screen = turtle.Screen()
screen.title('Gardi Fractal - PythonTurtle.Academy')
screen.setup(1000,1000)
screen.tracer(0,0)
turtle.hideturtle()
turtle.speed(0)
turtle.color('teal')

def circle(x,y,radius):
  turtle.up()
  turtle.goto(x,y-radius)
  turtle.down()
  turtle.seth(0)
  turtle.circle(radius, steps=360)

def two_circles(x,y,radius,orientation):
  turtle.pensize(radius/50)
  if orientation==0:
    circle(x-radius/2,y,radius)
    circle(x+radius/2,y,radius)
  else:
    circle(x,y-radius/2,radius)
    circle(x,y+radius/2,radius)

def gardi_fractal(x,y,radius,orientation,n):
  if n==0: return
  two_circles(x,y,radius,orientation)
  gardi_fractal(x,y,(4-7**0.5)/3*radius,1-orientation,n-1)
  
gardi_fractal(0,0,300,0,6)
screen.update()

turtle.mainloop() # Alt + F4