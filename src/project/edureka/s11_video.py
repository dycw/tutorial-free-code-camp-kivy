from kivy.app import App
from kivy.uix.video import Video


class SimpleApp(App):
    def build(self) -> Video:
        return Video(source="abc.mp4", play=True)


if __name__ == "__main__":
    SimpleApp().run()
