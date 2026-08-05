import turtle

ablak = turtle.Screen()
ablak.title("Nyomda")
ablak.bgcolor("black")

sanyi = turtle.Turtle()
sanyi.shape("turtle")
sanyi.color("lime")
sanyi.penup()
sanyi.goto(-400, 0)
sanyi.speed(0)

for _ in range(100):
    sanyi.stamp()
    sanyi.forward(50)

turtle.exitonclick()
