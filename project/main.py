from math import sin, cos, pi

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


Logger.info("Loaded")


class PlainPhisics(object):
    def __init__(self, gravity=.1, resistance=.05, speed_limit=20):
        super(PlainPhisics, self). __init__()
        self.gravity = gravity
        self.resistance = resistance
        self.speed_limit = speed_limit

    def process(self):
        for world_object in self.world_objects:
            world_object.move()
            world_object.velocity_x += world_object.acceleration_x * (
                world_object.velocity_x < self.speed_limit and world_object.velocity_x > -self.speed_limit)
            world_object.velocity_x *= 1. - self.resistance
            world_object.velocity_y += world_object.acceleration_y * (
                world_object.velocity_y < self.speed_limit and world_object.velocity_y > -self.speed_limit)
            world_object.velocity_y *= 1. - self.resistance
            world_object.acceleration_y = world_object.acceleration_y - self.gravity


class Movable(Widget):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    acceleration_x = NumericProperty(0)
    acceleration_y = NumericProperty(0)

    def move(self):
        self.x += self.velocity_x
        if self.x < 0:
            self.x = 0
            self.move_stop_x()
        self.y += self.velocity_y
        if self.y < 0:
            self.y = 0
            self.move_stop()

    def move_stop_x(self):
        self.velocity_x = self.acceleration_x = 0

    def move_stop_y(self):
        self.velocity_y = self.acceleration_y = 0

    def move_stop(self):
        self.move_stop_x()
        self.move_stop_y()


class Actor(Movable, Widget):
    pass


class Battlefield(PlainPhisics, Widget):

    actor = ObjectProperty(None)
    world_objects = ReferenceListProperty(actor)

    def on_touch_down(self, touch):
        angle = -Vector(1, 0).angle((touch.x - self.actor.x, touch.y - self.actor.y)) * pi / 180.
        distance = Vector(self.actor.x, self.actor.y).distance((touch.x, touch.y))
        self.actor.velocity_x = .07 * cos(angle) * distance
        self.actor.velocity_y = .07 * sin(angle) * distance
        Logger.info("%s" % self.actor.velocity)

    def update(self, x):
        self.process()


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
