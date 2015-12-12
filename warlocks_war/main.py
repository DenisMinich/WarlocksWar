from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget

from warlocks_war.objects import Collector, Actor, Terra, WorldObject, WidgetsCollection
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics
from warlocks_war.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(WorldObject):
    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.objects = WidgetsCollection([
            Actor(size=(40, 50), pos=(200, 200), foreground="mage.png")], self)
        gravity = PlainPhisics(gravity=(0, -.1), affect_objects=self.objects)
        self.phisics = WidgetsCollection([gravity], self)

    def update(self, *args, **kwargs):
        super(Battlefield, self).update(*args, **kwargs)



class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
