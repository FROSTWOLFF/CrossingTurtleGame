from turtle import Turtle


class Text(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(pos)
        self.level = 1
        self.update_level()

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def update_level(self):
        self.write(
            "Level : {}".format(self.level), align="center", font=("Arial", 20, "normal")
        )
