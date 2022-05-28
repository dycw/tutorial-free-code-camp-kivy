from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self) -> BoxLayout:
        layout = BoxLayout(orientation="vertical")
        layout.add_widget(Button(text="Hello World"))
        layout.add_widget(Button(text="Welcome to edureka"))
        return layout


if __name__ == "__main__":
    SimpleApp().run()
