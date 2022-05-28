from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout


class SimpleApp(App):
    def build(self) -> StackLayout:
        stack = StackLayout()
        for i in range(25):
            stack.add_widget(
                Button(text=str(i), width=100 + i * 5, size_hint=(None, 0.15))
            )
        return stack


if __name__ == "__main__":
    SimpleApp().run()
