import turtle
import random

# Háttér beállítása
bg = turtle.Screen()
bg.bgcolor("light blue")

# Teknős létrehozása
Sanyi = turtle.Turtle()

# Háromszög rajzolása
Sanyi.color("dark red")
Sanyi.penup()
Sanyi.goto(-30, 120)
Sanyi.begin_fill()
Sanyi.pendown()
Sanyi.goto(-140, -120)
Sanyi.forward(200)
Sanyi.left(110)
Sanyi.forward(260)
Sanyi.end_fill()

# Kör rajzolása a háromszög közepén
Sanyi.penup()
Sanyi.backward(40)
Sanyi.pendown()
Sanyi.begin_fill()
Sanyi.color("white")
Sanyi.right(80)
Sanyi.circle(30)
Sanyi.end_fill()

# Bojt rajzolása a háromszög aljára
Sanyi.penup()
Sanyi.goto(-142, -132)
Sanyi.pendown()
Sanyi.setheading(0)

# Bojt készítése kis körökkel
for _ in range(9):
    Sanyi.begin_fill()
    Sanyi.circle(13)
    Sanyi.end_fill()
    Sanyi.penup()
    Sanyi.forward(25)
    Sanyi.pendown()

# Üzenet kiírása
Sanyi.penup()
Sanyi.goto(0, -200)
Sanyi.color("gold")
Sanyi.write(
    "Csing ling ling száncsengő",
    font=("Lucida Handwriting", 18, "bold"),
    align="center",
)
Sanyi.color("white")
Sanyi.pendown()

# Hópehely rajzolása
def rajzolj_hopihet(meret):
    ag = meret / 3
    for i in range(6):
        Sanyi.forward(meret)
        Sanyi.backward(ag)
        Sanyi.right(30)
        Sanyi.forward(ag)
        Sanyi.backward(ag)
        Sanyi.left(60)
        Sanyi.forward(ag)
        Sanyi.backward(ag)
        Sanyi.right(30)
        Sanyi.backward(meret - ag)
        Sanyi.right(60)

# Véletlen helyre ugrás
def menj_veletlen_helyre():
    Sanyi.penup()
    Sanyi.goto(random.randint(-250, 250), random.randint(-250, 250))
    Sanyi.pendown()

Sanyi.pensize(4)
menj_veletlen_helyre()
rajzolj_hopihet(15)
menj_veletlen_helyre()
rajzolj_hopihet(20)
menj_veletlen_helyre()
rajzolj_hopihet(10)
menj_veletlen_helyre()
rajzolj_hopihet(17)
Sanyi.hideturtle()

# Klikkeléssel zárható ablak
turtle.exitonclick()
