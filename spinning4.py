from turtle import *
color('black', 'green')
begin_fill()
while True:
    forward(400)
    left(170)
    if abs(pos()) < 5:
        break
hideturtle()
end_fill()
done()
