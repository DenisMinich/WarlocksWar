from kivy.app import App
from kivy.clock import Clock
from kivy.resources import resource_add_path
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget

from warlocks_war.objects import Actor, ObjectsModel, Terra
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics
from warlocks_war.settings import STATIC_PATH

resource_add_path(STATIC_PATH)
Builder.load_file('game.kv')


class Battlefield(Widget):

    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.phisics_model = PhisicsModel(
            PlainPhisics(gravity=(0, -.1)),
            PointPhisics(gravity=.001, coords=(400, 300), affection_radius=200),
                PointPhisics(gravity=.01, coords=(200, 200), affection_radius=100))
        self.world_objects = ObjectsModel(
            Actor(size=(40, 50), pos=(150, 200), id="main_actor", foreground="mage.png"),
            parent_widget=self)
        self.terra = Terra(size=(220, 300), pos=(305, 135), foreground="bitmap_test.png")
        self.add_widget(self.terra)

    def on_touch_down(self, touch):
        Logger.info("On touch down")
        Logger.info("Terra collide: %s" % self.terra.collide_point(touch.x, touch.y))

    def update(self, x):
        self.phisics_model.process(self.world_objects)
        self.world_objects.update()


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
