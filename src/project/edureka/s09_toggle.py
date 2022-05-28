from kivy.app import App
from kivy.uix.togglebutton import ToggleButton


class SimpleApp(App):
    def build(self) -> ToggleButton:
        return ToggleButton(
            text="python", border=(26, 26, 26, 26), font_size=200
        )


if __name__ == "__main__":
    SimpleApp().run()
