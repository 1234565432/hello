import os
import turtle
os.chdir(r'D:\GitHub\hello')
brad = turtle.Turtle()
window = turtle.Screen()
window.bgcolor('red')
turtle.title('welcome to my wechat')
turtle.setup(width=512, height=512, startx=0, starty=0)
turtle.bgpic('my.gif')
brad.color('red')
brad.speed(0.8)
brad.shape('classic')
brad.dot(5,'red')
for i in range(0, 4, 1):
    brad.forward(100)
    brad.right(90)

ano = turtle.Turtle()
ano.speed(1)
ano.shape('arrow')
for i in range(0, 3, 1):
    ano.forward(100)
    ano.right(-120)
turtle.exitonclick()