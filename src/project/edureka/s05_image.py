from kivy.app import App
from kivy.uix.image import Image


class SimpleApp(App):
    def build(self) -> Image:
        return Image(source="logo.png")


if __name__ == "__main__":
    SimpleApp().run()
