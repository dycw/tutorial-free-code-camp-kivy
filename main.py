from typing import Any  # noqa: INP001

from kaki.app import App
from kivy.factory import Factory
from kivymd.app import MDApp


class MDLive(App, MDApp):
    CLASSES = {"Main": "project.the_lab"}
    AUTORELOADER_PATHS = [(".", {"recursive": True})]

    def build_app(self, first: bool = False) -> Any:
        _ = first

        return Factory.Main()


if __name__ == "__main__":
    MDLive().run()
