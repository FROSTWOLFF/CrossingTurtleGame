from turtle import Screen, Turtle


def go_up():
    turtle.forward(10)


# Screen properties
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(go_up, "w")

# Main Turtle properties
turtle = Turtle("turtle")
turtle.penup()
turtle.color("black")
turtle.setpos(0, -280)
turtle.setheading(90)

game_on = True
while game_on:
    screen.update()


screen.mainloop()