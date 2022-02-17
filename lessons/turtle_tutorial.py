from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

colormode(378)
leo.color("blue")

i: int = 0
while (i < 4):
    leo.forward(300)
    leo.left(90)
    i = i + 1


done()
