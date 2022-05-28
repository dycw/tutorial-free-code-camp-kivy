from random import random
from time import time

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import ListProperty
from kivy.uix.screenmanager import Screen
from kivy.uix.screenmanager import ScreenManager


class FirstScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class ColourScreen(Screen):
    colour = ListProperty([1.0, 0.0, 0.0, 1.0])


class MyScreenManager(ScreenManager):
    def new_colour_screen(self) -> None:
        name = str(time())
        self.add_widget(
            ColourScreen(
                name=name,
                colour=[random() for _ in range(3)] + [1],  # noqa: S311
            )
        )
        self.current = name


root_widget = Builder.load_string(
    """
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
MyScreenManager:
    transition: FadeTransition()
    FirstScreen:
    SecondScreen:
<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'first screen!'
            font_size: 30
        Image:
            source: 'logo.png'
            allow_stretch: False
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto second screen'
                font_size: 30
                on_release: app.root.current = 'second'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
<SecondScreen>:
    name: 'second'
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'second screen!'
            font_size: 30
        Image:
            source: 'logo1.jpg'
            allow_stretch: False
            keep_ratio: False
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
<ColourScreen>:
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: 'colour {:.2},{:.2},{:.2} screen'.format(*root.colour[:3])
            font_size: 30
        Widget:
            canvas:
                Color:
                    rgba: root.colour
                Ellipse:
                    pos: self.pos
                    size: self.size
        BoxLayout:
            Button:
                text: 'goto first screen'
                font_size: 30
                on_release: app.root.current = 'first'
            Button:
                text: 'get random colour screen'
                font_size: 30
                on_release: app.root.new_colour_screen()
"""
)


class ScreenManagerApp(App):
    def build(self) -> MyScreenManager:
        return root_widget


ScreenManagerApp().run()
