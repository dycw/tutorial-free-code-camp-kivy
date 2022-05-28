from typing import Any

from kivy import require
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget


require("2.1.0")  # replace with your current kivy version !


class MyApp(App):
    def build(self) -> Widget:
        return LoginScreen()


class LoginScreen(GridLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text="User Name"))
        self.add_widget(TextInput(multiline=False))
        self.add_widget(Label(text="password"))
        self.add_widget(TextInput(password=True, multiline=False))


if __name__ == "__main__":
    MyApp().run()
