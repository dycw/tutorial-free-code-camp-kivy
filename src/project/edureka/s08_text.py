from kivy.app import App
from kivy.uix.textinput import TextInput


class SimpleApp(App):
    def build(self) -> TextInput:
        return TextInput(font_size=150)


if __name__ == "__main__":
    SimpleApp().run()
