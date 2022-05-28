from kivy.app import App
from kivy.uix.checkbox import CheckBox


class SimpleApp(App):
    def build(self) -> CheckBox:
        checkbox = CheckBox()
        checkbox.bind(active=self._active)
        return checkbox

    @staticmethod
    def _active(checkbox: CheckBox, value: bool) -> None:
        if value:
            print(f"{checkbox=} is active")  # noqa: T201
        else:
            print(f"{checkbox=} is inactive")  # noqa: T201


if __name__ == "__main__":
    SimpleApp().run()
