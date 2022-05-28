from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ScatterTextWidget(BoxLayout):
    pass


class S24_KVApp(App):
    def build(self) -> ScatterTextWidget:
        return ScatterTextWidget()


if __name__ == "__main__":
    S24_KVApp().run()
