from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.stencilview import StencilView


class SimpleApp(App):
    def build(self) -> StencilView:
        stencil = StencilView()
        stencil.add_widget(sc := Scatter())
        sc.add_widget(Label(text="edureka"))
        return stencil


if __name__ == "__main__":
    SimpleApp().run()
