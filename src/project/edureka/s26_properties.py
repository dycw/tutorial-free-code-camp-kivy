from typing import Any

from kivy.app import App
from kivy.graphics import Color
from kivy.graphics import Ellipse
from kivy.uix.widget import Widget


class MyPaintWidget(Widget):
    def on_touch_down(self, touch: Any) -> None:
        with self.canvas:
            Color(1, 1, 0)
            d = 30.0
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))


class MyPaintApp(App):
    def build(self) -> MyPaintWidget:
        return MyPaintWidget()


if __name__ == "__main__":
    MyPaintApp().run()
