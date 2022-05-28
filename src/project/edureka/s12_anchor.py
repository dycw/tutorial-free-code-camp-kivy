from kivy.app import App
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self) -> AnchorLayout:
        layout = AnchorLayout(anchor_x="center", anchor_y="center")
        layout.add_widget(Button(text="Hello World"))
        return layout


if __name__ == "__main__":
    SimpleApp().run()
