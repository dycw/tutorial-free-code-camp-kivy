from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.scatter import Scatter


class SimpleApp(App):
    def build(self) -> Scatter:
        scatter = Scatter()
        scatter.add_widget(Image(source="logo.png"))
        return scatter


if __name__ == "__main__":
    SimpleApp().run()
