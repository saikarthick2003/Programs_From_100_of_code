import turtle as t
import random as r


screen = t.Screen()
screen.setup(400, 200)
user_bet = screen.textinput("Make your bet", "Which turtle will win this race")

turtle_colors = ["green","blue","yellow","red","black","purple","grey"]
y_position = [0,-20,20,-40,40,-60,60]
turtles = []
for i in range(0,7):
    tim = t.Turtle(shape="turtle")
    tim.color(turtle_colors[i])
    tim.penup()
    tim.goto(x=-180,y=y_position[i])
    turtles.append(tim)
    print(id(tim))
winner = ""
game_starts = False
if user_bet:
    game_starts = True


while game_starts:
    for t in turtles:
        t.forward(r.randrange(1,10))

        if t.xcor() >180:
            game_starts = False
            winner = t.pencolor()

if winner == user_bet:
    print("you won!")
else:
    print(f"you lost!, The winner is {winner}")


screen.exitonclick()




