from turtle import Screen, Turtle
from cars import Car, all_cars
import time


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
car_generate_counter = 0
while game_on:
    screen.update()

    # Its to lower the times of the cars are generated.
    if car_generate_counter % 5 == 0:
        Car.generate()

    for car in all_cars:
        car.move()

    car_generate_counter += 1
    time.sleep(0.1)

screen.mainloop()