# import colorgram
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
# for color in colors:
#    color_list.append(tuple(color.rgb))
# print(color_list)
from turtle import Turtle, Screen
import random

color_list = [(129, 165, 205), (223, 150, 110), (31, 40, 60), (201, 134, 146), (140, 185, 163), (236, 214, 93),
              (167, 60, 48), (35, 100, 151), (141, 64, 72), (236, 165, 156), (215, 86, 78), (171, 29, 32),
              (49, 113, 91), (231, 160, 164), (155, 34, 31), (170, 188, 221), (18, 96, 71), (29, 64, 59), (57, 51, 48),
              (51, 45, 48), (28, 60, 114), (104, 128, 161), (174, 200, 188), (34, 151, 210), (208, 92, 96),
              (65, 65, 57)]

screen = Screen()
screen.colormode(255)

cols = int(input("How many columns? "))
rows = int(input("How many rows? "))

turtle = Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.hideturtle()

lat = -400
long = -300

turtle.goto(lat, long)

for _ in range(rows):
    turtle.goto(lat, long)
    for _ in range(cols):
        turtle.dot(20, random.choice(color_list))
        turtle.forward((abs(lat) * 2) / (cols - 1))
    long += (abs(lat) * 2) / rows
screen.exitonclick()
