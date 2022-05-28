from random import random
from typing import Any

from kivy.animation import Animation
from kivy.base import runTouchApp
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.widget import Widget


Builder.load_string(
    """
<Root>:
    ARect:
        pos: 500, 300
<ARect>:
    canvas:
        Color:
            rgba: 0, 0, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
"""
)


class Root(Widget):
    pass


class ARect(Widget):
    def circle_pos(self) -> None:
        Animation.cancel_all(self)
        random_x = random() * (Window.width - self.width)  # noqa: S311
        random_y = random() * (Window.height - self.height)  # noqa: S311

        anim = Animation(x=random_x, y=random_y, duration=4, t="out_elastic")
        anim.start(self)

    def on_touch_down(self, touch: Any) -> None:
        if self.collide_point(*touch.pos):
            self.circle_pos()


if __name__ == "__main__":
    runTouchApp(Root())
