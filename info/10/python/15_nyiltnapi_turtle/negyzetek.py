import turtle

ablak = turtle.Screen()
ablak.title("Forgó négyzetek")
ablak.bgcolor("black")

sanyi = turtle.Turtle()
sanyi.speed(0)
sanyi.pensize(3)
sanyi.color("deepskyblue")

for i in range(72):
    for _ in range(4):
        sanyi.forward(i * 5)
        sanyi.right(90)
    sanyi.right(5)

turtle.exitonclick()
