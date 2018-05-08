import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_sjx(kk):
    kk.forward(100)
    kk.right(120)
    kk.forward(100)
    kk.right(120)
    kk.forward(100)

def draw_art():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()

    brad.shape("turtle")
    brad.color("black")
    brad.speed("10")
    # for i in range(1,37):
    #     draw_square(brad)
    #     brad.right(10)

    for i in range(1,37):
        draw_sjx(brad)
        brad.right(10)

    # brad.forward(100)
    # brad.right(90)
    #
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    # brad.forward(100)
    # brad.right(90)
    #
    # angie=turtle.Turtle()
    #
    # angie.shape("arrow")
    # angie.color("yellow")
    # angie.circle(100)
    #
    # kk=turtle.Turtle()
    # kk.shape("turtle")
    # kk.color("white")
    #
    # kk.forward(100)
    # kk.right(120)
    # kk.forward(100)
    # kk.right(120)
    # kk.forward(100)


    window.exitonclick()


draw_art()
