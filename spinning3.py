from turtle import*
import turtle
setup()
t1=Turtle()
color=("red","yellow","green","blue","orange","pink","black","grey")
import random
t1.up()
t1.goto(-200,0)
t1.down()
t1.width(5)
t1.hideturtle()
t1.speed(0)
for i in range(900):
    colorchoice=random.choice(color)
    t1.color(colorchoice)
    t1.forward(400)
    t1.left(181)
