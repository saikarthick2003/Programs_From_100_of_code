import colorgram as color
import turtle as t
import random as r
# colors = color.extract('Isocytosine-Website.jpg',43)
# rgb_values = []
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     t = (r,g,b)
#     rgb_values.append(t)
#
# print(rgb_values)
color_values = [(238, 237, 237), (237, 235, 237), (229, 234, 239), (226, 206, 84), (216, 233, 217), (65, 78, 138), (204, 134, 159), (166, 46, 82), (114, 163, 217), (146, 67, 50), (220, 152, 61), (155, 33, 66), (160, 154, 47), (161, 218, 180), (200, 82, 125), (6, 66, 154), (212, 83, 56), (159, 181, 229), (102, 50, 39), (91, 126, 206), (154, 202, 226), (218, 173, 190), (220, 177, 171), (77, 53, 44), (225, 202, 28), (0, 61, 127)]
def draw_circle(circlesize):
    tom.pendown()
    tom.pencolor(fill)
    tom.fillcolor(fill)
    tom.begin_fill()
    tom.circle(circlesize)
    tom.end_fill()
    tom.penup()
def move_to_next_row():
    tom.setheading(90)
    tom.forward(50)
    tom.setheading(180)
    tom.forward((10 * 50))
    tom.setheading(360)

tom = t.Turtle()
tom.penup()
tom.goto((-120, -120))
tom.pendown()
t.colormode(255)
tom.speed(0)
for i in range(10):
    for i in range(10):
        fill = r.choice(color_values)
        draw_circle(20)
        tom.forward(50)
    move_to_next_row()





screen = t.Screen()
screen.exitonclick()

