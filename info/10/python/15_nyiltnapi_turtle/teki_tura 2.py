import turtle
import random

ablak = turtle.Screen()
ablak.title("Teki túra")
ablak.bgcolor("white")

sanyi = turtle.Turtle()
sanyi.pensize(4)
sanyi.speed(0)

szinek = ["orange", "green", "blue", "red", "pink"]

for _ in range(20):
    irany = random.randint(1, 3)
    sanyi.color(random.choice(szinek))
    if irany == 1:
        sanyi.forward(50)
    elif irany == 2:
        sanyi.right(90)
        sanyi.forward(50)
    else:
        sanyi.left(90)
        sanyi.forward(50)

turtle.exitonclick()
