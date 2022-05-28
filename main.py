from typing import Any  # noqa: INP001

import kaki.app
import kivy.app
from kivy.factory import Factory
from kivy.uix.widget import Widget
from kivymd.app import MDApp

from project.the_lab import Main


class MDLive(kaki.app.App, MDApp):
    CLASSES = {"Main": "project.the_lab"}
    AUTORELOADER_PATHS = [(".", {"recursive": True})]

    def build_app(self, first: bool = False) -> Any:
        _ = first

        return Factory.Main()


class Entry(kivy.app.App):
    def build(self) -> Widget:
        return Main()


if __name__ == "__main__":
    Entry().run()
    # MDLive().run()
