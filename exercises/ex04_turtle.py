"""A Sunny day in the City."""

__author__ = "730475811"

from turtle import Turtle, colormode, done


def main() -> None: 
    """The beautiful city scenery created by the following hardworking dear turtles."""
    city_turtle: Turtle = Turtle()  # the turtle representing the whole city
    city_turtle.speed(50)
    colormode(255)
    city_turtle.color(153, 192, 236)
    draw_rectangle(city_turtle, -1000, 1000, 2000, 1100)  # sky turtle
    city_turtle.color(133, 109, 84)
    draw_rectangle(city_turtle, -1000, -100, 2000, 1000)  # ground turtle
    city_turtle.pencolor(22, 22, 21)
    city_turtle.fillcolor(104, 98, 87)
    draw_rectangle(city_turtle, -500, -100, 110, -300)  # outlined and filled in building turtles 19-22
    draw_rectangle(city_turtle, -250, -100, 110, -300)
    draw_rectangle(city_turtle, 250, -100, 110, -300)
    draw_rectangle(city_turtle, 500, -100, 110, -300)
    city_turtle.color(60, 39, 35)
    draw_rectangle(city_turtle, 35, -100, 35, 100)  # treetrunk turtle
    city_turtle.color(114, 156, 85)
    draw_triangle(city_turtle, 0, 0, 100)  # tree turtle 26-28
    draw_triangle(city_turtle, 0, -50, 100)
    draw_triangle(city_turtle, 0, -100, 100)
    city_turtle.pencolor(222, 93, 52)
    city_turtle.fillcolor(242, 229, 35)
    draw_circle(city_turtle, 0, 300, 50)  # outlined and filles sun turtle
    city_turtle.color(63, 129, 132)
    draw_square(city_turtle, -450, 100, 50,)  # window turtle 33-36
    draw_square(city_turtle, -200, 100, 50,)
    draw_square(city_turtle, 260, 100, 50,)
    draw_square(city_turtle, 510, 100, 50,)
    city_turtle.hideturtle()
    done()


def draw_rectangle(building_turtle: Turtle, x: float, y: float, width: float, height: float) -> None:
    """Turtle the builder, drawing rectangles by having two loops in order to have two different sizes (length and width)."""
    building_turtle.penup()
    building_turtle.begin_fill()
    building_turtle.goto(x, y) 
    building_turtle.setheading(0.0)
    building_turtle.pendown()
    i: int = 0
    while i < 2:
        building_turtle.forward(width)
        building_turtle.right(90)
        i = i + 1
        building_turtle.forward(height)
        building_turtle.right(90)
    building_turtle.end_fill()
    building_turtle.penup()


def draw_square(window_turtle: Turtle, x: float, y: float, width: float) -> None:
    """Draw a square of the given width whose top-left corner is located at x, y. four loops for each side."""
    window_turtle.penup()
    window_turtle.begin_fill()
    window_turtle.goto(x, y) 
    window_turtle.setheading(0.0)
    window_turtle.pendown()
    i: int = 0
    while i < 4:
        window_turtle.forward(width)
        window_turtle.right(90)
        i = i + 1
    window_turtle.end_fill()
    window_turtle.penup()


def draw_triangle(tree_turtle: Turtle, x: float, y: float, length: float) -> None:
    """Drawing triangles with a while loop < 3 representing the three sides and the triangles are equailateral."""
    tree_turtle.penup()
    tree_turtle.begin_fill()
    tree_turtle.goto(x, y) 
    tree_turtle.setheading(0.0)
    tree_turtle.pendown()
    i: int = 0
    while i < 3:
        tree_turtle.forward(length)
        tree_turtle.left(120)
        i = i + 1
    tree_turtle.end_fill()
    tree_turtle.penup()


def draw_circle(sun_turtle: Turtle, x: int, y: int, radius: int) -> None:
    """Drawing the sun using a circle function with (x, y) for location and radius as the determinant for the size."""
    sun_turtle.penup()
    sun_turtle.begin_fill()
    sun_turtle.goto(x, y) 
    sun_turtle.setheading(0.0)
    sun_turtle.pendown()
    sun_turtle.circle(radius)
    sun_turtle.end_fill()
    sun_turtle.penup()


if __name__ == "__main__":
    main()
