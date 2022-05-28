from kivy.app import App
from kivy.uix.switch import Switch


class SimpleApp(App):
    def build(self) -> Switch:
        return Switch(active=True)


if __name__ == "__main__":
    SimpleApp().run()
