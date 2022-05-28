from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class SimpleApp(App):
    def build(self) -> GridLayout:
        layout = GridLayout(cols=2)
        layout.add_widget(Button(text="hello"))
        layout.add_widget(Button(text="world"))
        layout.add_widget(Button(text="welcome to"))
        layout.add_widget(Button(text="edureka"))
        return layout


if __name__ == "__main__":
    SimpleApp().run()
