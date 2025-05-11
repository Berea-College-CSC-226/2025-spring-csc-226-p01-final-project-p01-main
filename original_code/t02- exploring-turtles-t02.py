import turtle
wn = turtle.Screen()
wn.bgcolor("green")
shay = turtle.Turtle()

#Set up F turtle
shay.pensize(9)
shay.color("yellow")

#Draw the F
shay.penup()
shay.backward(100)
shay.pendown()
shay.left(90)
shay.forward(150)
shay.right(90)
shay.forward(90)
shay.penup()
shay.right(90)
shay.forward(70)
shay.right(90)
shay.forward(20)
shay.pendown()
shay.forward(70)

#Set up B turtle
sania = turtle.Turtle()
sania.color("pink")
sania.pensize(9)

#Draw the B
sania.penup()
sania.forward(30)
sania.pendown()
sania.left(90)
sania.forward(150)
sania.right(90)
sania.forward(20)

for _ in range(18):
    sania.forward(6)
    sania.right(10)

sania.forward(20)

sania.right(180)
sania.forward(20)

for _ in range(18):
    sania.forward(7.1)
    sania.right(10)

sania.forward(30)
wn.exitonclick()