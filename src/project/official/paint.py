from random import random
from typing import Any

from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.graphics import Line
from kivy.uix.button import Button
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):
    def on_touch_down(self, touch: Any) -> None:
        color = (random(), random(), random())  # noqa: S311
        with self.canvas:
            Color(*color)
            d = 30.0
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud["line"] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch: Any) -> None:
        touch.ud["line"].points += [touch.x, touch.y]


class MyPaintApp(App):
    def build(self) -> Widget:
        parent = Widget()
        self.painter = MyPaintWidget()
        clearbtn = Button(text="Clear")
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent

    def clear_canvas(self, obj: Any) -> None:  # noqa: U100
        self.painter.canvas.clear()


if __name__ == "__main__":
    MyPaintApp().run()
