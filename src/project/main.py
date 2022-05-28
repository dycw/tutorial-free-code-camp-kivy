from typing import Any

from kivy import require
from kivy.app import App
from kivy.graphics.vertex_instructions import Rectangle
from kivy.properties import NumericProperty
from kivy.properties import ReferenceListProperty
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.vector import Vector


require("2.1.0")  # replace with your current kivy version !


class PongApp(App):
    def build(self) -> "PongGame":
        return PongGame()


class PongGame(Widget):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        with self.canvas:
            Rectangle(pos=(self.center_x - 5, 0.0), size=(10, self.height))
            _ = Label(
                font_size=70,
                center_x=self.width / 4,
                top=self.top - 50.0,
                text="0",
            )
            _ = Label(
                font_size=70,
                center_x=self.width * 3 / 4,
                top=self.top - 50.0,
                text="0",
            )
            _ = PongBall(center=super().center)


class PongBall(Widget):
    # velocity of the ball on x and y axis
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property so we can use ball.velocity as
    # a shorthand, just like e.g. w.pos for w.x and w.y
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # ``move`` function will move the ball one step. This
    #  will be called in equal intervals to animate the ball
    def move(self) -> None:
        self.pos = Vector(*self.velocity) + self.pos


if __name__ == "__main__":
    PongApp().run()
