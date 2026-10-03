import turtle

ablak = turtle.Screen()
ablak.title("Színes csillagszóró")
ablak.bgcolor("black")

sanyi = turtle.Turtle()
sanyi.speed(0)
sanyi.pensize(4)

for i in range(144):
    if i % 2 == 0:
        sanyi.color("yellow")
    else:
        sanyi.color("red")
    sanyi.forward(150)
    sanyi.backward(150)
    sanyi.right(2.5)

turtle.exitonclick()
