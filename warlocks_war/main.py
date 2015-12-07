from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget

from warlocks_war.objects import Collector, Actor, ObjectsModel, Terra
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics
from warlocks_war.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(Widget):

    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)

        Collector.assign_collection("world_objects", ObjectsModel(parent_widget=self))
        Collector.assign_collection("world_phisics", PhisicsModel(parent_widget=self))

        PlainPhisics(gravity=(0, -.1))

        Terra(
            size=(300, 300),
            pos=(305, 135),
            foreground="triangle.png",
            bitmap="/home/gantz/projects/WarlocksWar/static/triangle.csv",
            mass=None)

    def on_touch_down(self, touch):
        Logger.info("On touch down")
        Actor(size=(40, 50), pos=(touch.x, touch.y), foreground="mage.png")

    def update(self, x):
        Collector.get_collection("world_phisics").process(
            Collector.get_collection("world_objects"))
        Collector.get_collection("world_objects").update()


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./10)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
