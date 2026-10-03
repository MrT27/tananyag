import turtle

ablak = turtle.Screen()
ablak.title("Színes spirál")
ablak.bgcolor("black")

sanyi = turtle.Turtle()
sanyi.speed(0)
sanyi.pensize(4)

for i in range(100):
    if i % 2 == 0:
        sanyi.color("blue")
    else:
        sanyi.color("orange")
    sanyi.forward(5 * i)
    sanyi.right(90)

turtle.exitonclick()
