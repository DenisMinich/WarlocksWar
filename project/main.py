from math import sin, cos, pi

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger
from kivy.properties import ObjectProperty, ReferenceListProperty, NumericProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector


Logger.info("Loaded")


class PhisicsModel(object):

    def __init__(self, phisics_objects=None, speed_limit=10.):
        super(PhisicsModel, self).__init__()
        self.phisics_objects = [] if phisics_objects is None else phisics_objects
        self.speed_limit = speed_limit

    def _get_acceleration(self, world_object):
        acceleration = Vector(0, 0)
        for phisics_object in self.phisics_objects:
            acceleration += phisics_object.get_acceleration(world_object)
        return acceleration

    def _update_velocity(self, world_object, acceleration):
        world_object.velocity = Vector(*world_object.velocity) + Vector(*acceleration)
        velocity_vector = Vector(world_object.velocity)
        if velocity_vector.length() > self.speed_limit:
            world_object.velocity = velocity_vector * self.speed_limit / velocity_vector.length()

    def process(self, world_objects):
        for world_object in world_objects:
            acceleration = self._get_acceleration(world_object)
            self._update_velocity(world_object, acceleration)
            world_object.move()


class PointPhisics(object):

    def __init__(self, gravity=0, coords=(0, 0), affection_radius=0):
        super(PointPhisics, self). __init__()
        self.gravity = gravity
        self.coords = Vector(coords)
        self.affection_radius = affection_radius

    def get_acceleration(self, world_object):
        acceleration_vector = Vector(self.coords.x - world_object.x, self.coords.y - world_object.y)
        if self.affection_radius < acceleration_vector.length():
            acceleration_vector *= 0
        else:
            acceleration_vector *= (1 - acceleration_vector.length() / self.affection_radius) * self.gravity
        return acceleration_vector


class PlainPhisics(object):

    def __init__(self, gravity=(0, 0)):
        super(PlainPhisics, self). __init__()
        self.gravity = Vector(gravity)

    def get_acceleration(self, world_object):
        return self.gravity


class Movable(Widget):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self, acceleration=0):
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


class Battlefield(Widget):

    def __init__(self, *args, **kwargs):
        super(Battlefield, self).__init__(*args, **kwargs)
        self.phisics_model = PhisicsModel(phisics_objects=[
            PlainPhisics(gravity=(0, -.1)),
            PointPhisics(gravity=.001, coords=(400, 300), affection_radius=200),
            PointPhisics(gravity=.01, coords=(200, 200), affection_radius=100)])

    actor = ObjectProperty(None)
    world_objects = ReferenceListProperty(actor)

    def on_touch_down(self, touch):
        self.actor.move_stop()
        angle = -Vector(1, 0).angle((touch.x - self.actor.x, touch.y - self.actor.y)) * pi / 180.
        distance = Vector(self.actor.x, self.actor.y).distance((touch.x, touch.y))
        self.actor.velocity_x = .03 * cos(angle) * distance
        self.actor.velocity_y = .03 * sin(angle) * distance

    def update(self, x):
        self.phisics_model.process(self.world_objects)


class GameApp(App):
    def build(self):
        battlefield = Battlefield()
        Clock.schedule_interval(battlefield.update, 1./60)
        return battlefield


if __name__ == "__main__":
    GameApp().run()
