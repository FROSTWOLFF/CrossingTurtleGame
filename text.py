from turtle import Turtle


class Text(Turtle):
    def __init__(self, pos=(0, 0)):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.setpos(pos)
        self.level = 1
        # self.update_level()

    @staticmethod
    def game_over():
        """Writes Game Over at the middle of the screen"""
        over = Text()
        over.write(
            "Game Over",
            align="center",
            font=("Arial", 40, "normal"),
        )

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def update_level(self):
        self.write(
            "Level : {}".format(self.level),
            align="center",
            font=("Arial", 20, "normal"),
        )
