from typing import Any
from typing import Literal
from typing import Optional

from beartype import beartype
from kivy.app import App
from kivy.input.providers.mouse import MouseMotionEvent
from kivy.properties import ListProperty
from kivy.properties import ObservableList
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget


require("2.1.0")  # replace with your current kivy version !


class RootWidget(BoxLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.add_widget(Button(text="btn 1"))
        cb = CustomBtn()
        cb.bind(pressed=self.btn_pressed)  # type: ignore
        self.add_widget(cb)
        self.add_widget(Button(text="btn 2"))

    @beartype
    def btn_pressed(self, _: "CustomBtn", pos: ObservableList) -> None:
        print(f"pos: printed from root widget: {pos}")  # noqa: T201


class CustomBtn(Widget):
    pressed = ListProperty([0, 0])

    @beartype
    def on_touch_down(self, touch: MouseMotionEvent) -> Optional[Literal[True]]:
        if self.collide_point(*touch.pos):
            self.pressed = touch.pos
            # we consumed the touch. return False here to propagate
            # the touch further to the children.
            return True
        return super().on_touch_down(touch)

    @beartype
    def on_pressed(self, _: "CustomBtn", pos: ObservableList) -> None:
        print(f"pressed at {pos}")  # noqa: T201


class TestApp(App):
    @beartype
    def build(self) -> RootWidget:
        return RootWidget()


if __name__ == "__main__":
    TestApp().run()
