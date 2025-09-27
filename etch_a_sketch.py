import turtle as t

def move_forward():
    t.fd(20)
def move_backward():
    t.back(20)
def anticlockwise():
    t.right(20)

def clockwise():
    t.left(20)
def delete():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


t.onkey(move_forward,"w")
t.onkey(move_backward,"s")
t.onkey(anticlockwise,"a") #anti-clock wise
t.onkey(clockwise,"d")
t.onkey(delete,"c")
t.listen()

screen = t.Screen()
screen.exitonclick()

