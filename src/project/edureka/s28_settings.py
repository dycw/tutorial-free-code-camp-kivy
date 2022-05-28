from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


Builder.load_string(
    """
<Interface>:
    orientation: 'vertical'
    Button:
        text: 'Settings'
        font_size: 100
        on_release: app.open_settings()
"""
)


class Interface(BoxLayout):
    pass


class SettingsApp(App):
    def build(self) -> Interface:
        return Interface()


if __name__ == "__main__":
    SettingsApp().run()
