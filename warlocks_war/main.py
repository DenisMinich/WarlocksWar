from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.logger import Logger
from kivy.uix.widget import Widget

from warlocks_war.objects import Actor, ObjectsModel
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics

Builder.load_file('game.kv')


from warlocks_war.objects import BitmapShape, EllipseShape


class TestBitmap(Actor, BitmapShape):
    pass


class Battlefield(Widget):

    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.phisics_model = PhisicsModel(
            PlainPhisics(gravity=(0, -.1)),
            PointPhisics(gravity=.001, coords=(400, 300), affection_radius=200),
            PointPhisics(gravity=.01, coords=(200, 200), affection_radius=100))
        self.world_objects = ObjectsModel(
            Actor(size=(10, 20), pos=(150, 200), id="main_actor"),
            parent_widget=self)
        self.bitmap = TestBitmap(size=(200, 200), pos=(300, 100), bitmap=EllipseShape.get_matrix(200, 200))
        self.add_widget(self.bitmap)

    def on_touch_down(self, touch):
        Logger.info("Collide bitmap - %s" % self.bitmap.collide_point(touch.x, touch.y))

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
