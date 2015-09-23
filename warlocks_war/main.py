from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.uix.widget import Widget

from warlocks_war.objects import Actor, ObjectsModel
from warlocks_war.phisics import PhisicsModel, PlainPhisics, PointPhisics

Builder.load_file('game.kv')


class Battlefield(Widget):

    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.phisics_model = PhisicsModel(
            PlainPhisics(gravity=(0, -.1)),
            PointPhisics(gravity=.001, coords=(400, 300), affection_radius=200),
            PointPhisics(gravity=.01, coords=(200, 200), affection_radius=100))
        self.world_objects = ObjectsModel(
            Actor(pos=(100, 300), id="main_actor"),
            parent_widget=self)

    def on_touch_down(self, touch):
        self.world_objects.append(Actor(pos=(touch.x, touch.y)))

    def update(self, x):
        self.phisics_model.process(self.world_objects)


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
