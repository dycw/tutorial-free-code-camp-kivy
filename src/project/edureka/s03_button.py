from kivy.app import App
from kivy.uix.button import Button


class SimpleApp(App):
    def build(self) -> Button:
        btn = Button(text="Edureka!", font_size=150)
        btn.bind(state=self._state)
        return btn

    @staticmethod
    def _state(instance: Button, value: str) -> None:
        print(f"Hello; {instance=}, {value=}")  # noqa: T201


if __name__ == "__main__":
    SimpleApp().run()
