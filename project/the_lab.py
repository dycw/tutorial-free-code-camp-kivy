from typing import Any

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Main(BoxLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b1.size = ("40dp", "40dp")
        b1.size_hint = (None, None)
        b2 = Button(text="B")
        b2.size_hint = (1.0, 3.0)
        b3 = Label(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
