from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput


class SimpleApp(App):
    def build(self) -> BoxLayout:
        box = BoxLayout(orientation="vertical")
        box.add_widget(
            text := TextInput(
                font_size=100, text="default", size_hint_y=None, height=100
            )
        )
        box.add_widget(flt := FloatLayout())
        flt.add_widget(scatter := Scatter())
        scatter.add_widget(label := Label(text="default", font_size=150))

        text.bind(text=label.setter("text"))
        return box


if __name__ == "__main__":
    SimpleApp().run()
