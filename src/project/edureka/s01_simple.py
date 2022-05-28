from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter


class SimpleApp(App):
    def build(self) -> FloatLayout:
        flt = FloatLayout()
        flt.add_widget(scatter := Scatter())
        scatter.add_widget(Label(text="Edureka!", font_size=150))
        return flt


if __name__ == "__main__":
    SimpleApp().run()
