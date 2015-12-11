from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget

from warlocks_war.objects import Collector, Actor, Terra, ObjectsCollection
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics
from warlocks_war.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(ObjectsCollection):
    def on_touch_down(self, touch):
        self.inner_objects.append(
            Actor(size=(40, 50), pos=(touch.x, touch.y), foreground="mage.png"))


class GameApp(App):
    def build(self):
        PlainPhisics(gravity=(0, -.1))
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
