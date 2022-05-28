from random import random
from typing import Any

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Text(BoxLayout):
    def change_label_colour(self, *_: Any) -> None:
        colour = [random() for _ in range(3)] + [1]  # noqa: S311
        label = self.ids["my_label"]
        label.color = colour


class S25_Python_And_KivyApp(App):
    def build(self) -> Text:
        return Text()


if __name__ == "__main__":
    S25_Python_And_KivyApp().run()
