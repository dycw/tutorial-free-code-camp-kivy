from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout


res = Builder.load_string(
    """BoxLayout:
    Label:
        text: 'Left'
    Button:
        text: 'Middle'
        on_touch_down: print('Middle: {}'.format(args[1].pos))
    RelativeLayout:
        on_touch_down: print('Relative: {}'.format(args[1].pos))
        Button:
            text: 'Right'
            on_touch_down: print('Right: {}'.format(args[1].pos))"""
)


class SimpleApp(App):
    def build(self) -> BoxLayout:
        return res


if __name__ == "__main__":
    SimpleApp().run()
