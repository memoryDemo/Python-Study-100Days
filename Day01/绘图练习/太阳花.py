# coding=utf-8
import turtle
import time

turtle.pencolor("red")
turtle.fillcolor("yellow")

turtle.begin_fill()
for _ in range(50):
    turtle.forward(200)
    turtle.left(170)
turtle.end_fill()
time.sleep(2)

turtle.mainloop()
