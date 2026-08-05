import turtle

ablak = turtle.Screen()
ablak.title("Karácsonyfa")
ablak.bgcolor("midnight blue")

teki = turtle.Turtle()
teki.speed(0)
teki.pensize(3)
teki.hideturtle()


def menj_oda(x, y):
    teki.penup()
    teki.goto(x, y)
    teki.pendown()


def teglalap(x, y, szelesseg, magassag, szin):
    menj_oda(x, y)
    teki.color(szin)
    teki.begin_fill()
    for _ in range(2):
        teki.forward(szelesseg)
        teki.left(90)
        teki.forward(magassag)
        teki.left(90)
    teki.end_fill()


def haromszog(x, y, alap, magassag, szin):
    menj_oda(x, y)
    teki.color(szin)
    teki.begin_fill()
    teki.forward(alap)
    teki.goto(x + alap / 2, y + magassag)
    teki.goto(x, y)
    teki.end_fill()


def csillag(x, y, hossz, szin):
    menj_oda(x, y)
    teki.setheading(90)
    teki.color(szin)
    teki.begin_fill()
    for _ in range(5):
        teki.forward(hossz)
        teki.right(144)
        teki.forward(hossz)
        teki.left(72)
    teki.end_fill()


def gomb(x, y, sugar, szin):
    menj_oda(x, y)
    teki.color(szin)
    teki.begin_fill()
    teki.circle(sugar)
    teki.end_fill()


# Törzs
teglalap(-25, -250, 50, 90, "saddlebrown")

# Lombkorona rétegei
haromszog(-160, -190, 320, 150, "forest green")
haromszog(-130, -120, 260, 140, "green")
haromszog(-100, -55, 200, 125, "dark green")

# Díszek
gomb(-95, -150, 10, "gold")
gomb(55, -150, 10, "red")
gomb(-20, -115, 10, "deepskyblue")
gomb(70, -80, 10, "orange")
gomb(-70, -65, 10, "violet")
gomb(0, -35, 10, "silver")

# Csúcsdísz
csillag(-18, 75, 22, "gold")

# Talaj / hó
teki.penup()
teki.goto(-350, -250)
teki.pendown()
teki.color("white")
teki.pensize(6)
teki.forward(700)

# Üzenet
menj_oda(-140, 170)
teki.color("white")
teki.write("Kellemes karácsonyt!", font=("Arial", 20, "bold"))

turtle.exitonclick()
