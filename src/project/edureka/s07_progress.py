from kivy.app import App
from kivy.uix.progressbar import ProgressBar


class SimpleApp(App):
    def build(self) -> ProgressBar:
        bar = ProgressBar(max=1000)
        bar.value = 650
        return bar


if __name__ == "__main__":
    SimpleApp().run()
