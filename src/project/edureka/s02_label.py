from kivy.app import App
from kivy.uix.label import Label


class SimpleApp(App):
    def build(self) -> Label:
        return Label(text="Edureka!", font_size=150)


if __name__ == "__main__":
    SimpleApp().run()
