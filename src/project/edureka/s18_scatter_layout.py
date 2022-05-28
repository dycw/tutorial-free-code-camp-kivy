from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatterlayout import ScatterLayout


class SimpleApp(App):
    def build(self) -> ScatterLayout:
        scatter = ScatterLayout()
        scatter.add_widget(Label(text="edureka"))
        return scatter


if __name__ == "__main__":
    SimpleApp().run()
