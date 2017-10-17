__version__ = 1.0
def draw_square():
    '''hahaa
    hehehe'''
    import os
    import turtle
    os.chdir(r'D:\GitHub\hello')
    brad = turtle.Turtle()
    window = turtle.Screen()
    window.bgcolor('red')
    turtle.title('welcome to my wechat')
    turtle.setup(width=512, height=512, startx=960 - 206, starty=540 - 206)
    turtle.bgpic('my.gif')
    brad.color('red')
    brad.pensize(5)
    brad.speed(0.8)
    brad.shape('classic')
    brad.dot(5, 'red')
    for i in range(0, 4, 1):
        brad.forward(100)
        brad.right(90)
    print('doc', draw_square.__doc__)
    ano = turtle.Turtle()
    ano.speed(1)
    ano.pensize(10)
    ano.shape('arrow')
    for i in range(0, 3, 1):
        ano.forward(100)
        ano.right(-120)
    turtle.exitonclick()
draw_square()
print(draw_square.__doc__)
__version__ = 1.0
dir()
