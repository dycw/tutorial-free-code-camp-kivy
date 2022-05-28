from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout


class SimpleApp(App):
    def build(self) -> PageLayout:
        layout = PageLayout()
        layout.add_widget(Button(text="hello", background_color=(1, 0, 0, 1)))
        layout.add_widget(Button(text="world", background_color=(0, 1, 0, 1)))
        layout.add_widget(
            Button(text="welcome to", background_color=(1, 1, 1, 1))
        )
        layout.add_widget(Button(text="edureka", background_color=(0, 1, 1, 1)))
        return layout


if __name__ == "__main__":
    SimpleApp().run()
