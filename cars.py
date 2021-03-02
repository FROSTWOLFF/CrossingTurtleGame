from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
START_X = 320

# globals
car_speed = 10
all_cars = []


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)

    # @staticmethod
    # def reset():
    #     all_cars.clear()

    @staticmethod
    def level_up():
        global car_speed
        car_speed += 5

    @staticmethod
    def generate():
        rand_y = random.randint(-240, 300)
        rand_color = random.choice(COLORS)

        new_car = Car()
        new_car.color(rand_color)
        new_car.setpos(START_X, rand_y)
        all_cars.append(new_car)

    def move(self):
        self.forward(car_speed)
