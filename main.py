from turtle import Screen, Turtle
from cars import Car, all_cars
from text import Text
import time

START_POS = (0, -280)
LEVEL_TEXT_POS = (-240, 255)


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
turtle.setpos(START_POS)
turtle.setheading(90)


text = Text(LEVEL_TEXT_POS)


game_on = True
car_generate_counter = 0
while game_on:
    screen.update()

    # It's to lower the times of the cars that are generated.
    if car_generate_counter % 5 == 0:
        Car.generate()

    for car in all_cars:
        car.move()

    # Level Passed
    if turtle.ycor() > 280:
        Car.level_up()
        text.level_up()

        turtle.setpos(START_POS)

    car_generate_counter += 1
    time.sleep(0.1)

screen.mainloop()