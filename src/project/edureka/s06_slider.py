from kivy.app import App
from kivy.uix.slider import Slider


class SimpleApp(App):
    def build(self) -> Slider:
        return Slider(
            orientation="vertical",
            value_track=True,
            value_track_color=(1, 0, 0, 1),
        )


if __name__ == "__main__":
    SimpleApp().run()
