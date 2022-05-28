from string import ascii_uppercase
from typing import Any

from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.pagelayout import PageLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.stacklayout import StackLayout


class Main(GridLayout):
    count = 1
    my_text = StringProperty("1")

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(cols=3, **kwargs)

        self.add_widget(button := Button(text="Click here"))
        button.on_press = self.on_button_click
        self.add_widget(Label(text=self.my_text))

    def on_button_click(self) -> None:
        self.my_text = f"{self.count}"
        self.count += 1


class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(orientation="horizontal", **kwargs)

        self.add_widget(
            Button(text="A", size_hint=(0.5, 0.5), pos_hint={"center_y": 0.5})
        )

        self.add_widget(
            box := BoxLayout(orientation="vertical", spacing="10dp")
        )
        for i in range(1, 5):
            box.add_widget(Button(text=f"B{i}"))

        self.add_widget(Label(text="C", color="black"))


class AnchorLayoutExample(AnchorLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(anchor_x="center", anchor_y="top", **kwargs)

        self.add_widget(box := BoxLayout(size_hint=(0.2, 0.2)))
        for text in ascii_uppercase[:2]:
            box.add_widget(Button(text=text))


class GridLayoutExample(GridLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(cols=3, **kwargs)
        for text in ascii_uppercase[:6]:
            if text in {"A", "D"}:
                self.add_widget(
                    Button(text=text, size_hint=(None, 1.0), width=dp(60))
                )
            elif text == "B":
                self.add_widget(BoxLayoutExample())
            else:
                self.add_widget(Button(text=text))


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        size = dp(100)
        for i in range(100):
            self.add_widget(
                Button(
                    text=format(i + 1),
                    size=(size, size),
                    size_hint=(None, None),
                )
            )


class ScrollViewExample(ScrollView):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self.add_widget(stack := StackLayoutExample(size_hint=(1.0, None)))
        self.height = stack.minimum_height


class PageLayoutExample(PageLayout):
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)

        self.add_widget(BoxLayoutExample())
        self.add_widget(AnchorLayout())
        self.add_widget(GridLayout())
        self.add_widget(StackLayoutExample())
        self.add_widget(ScrollViewExample())
