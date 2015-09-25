from kivy.properties import NumericProperty, ReferenceListProperty, BooleanProperty
from kivy.vector import Vector

from warlocks_war.objects.world_object import WorldObject


class Movable(WorldObject):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acceleration_x = NumericProperty(0)
    acceleration_y = NumericProperty(0)
    acceleration = ReferenceListProperty(acceleration_x, acceleration_y)
    in_move = BooleanProperty(False)

    def __init__(self, *args, speed_limit=10., **kwargs):
        super(Movable, self).__init__(*args, **kwargs)
        self.speed_limit = speed_limit
        self.register_event_type('on_move')
        self.register_event_type('on_move_x')
        self.register_event_type('on_move_y')
        self.register_event_type('on_stop')
        self.register_event_type('on_stop_x')
        self.register_event_type('on_stop_y')
        self.bind(on_update=self.move)

    def _update_velocity(self):
        self.velocity = Vector(*self.velocity) + Vector(*self.acceleration)
        velocity_vector = Vector(self.velocity)
        if velocity_vector.length() > self.speed_limit:
            self.velocity = velocity_vector * self.speed_limit / velocity_vector.length()

    def move(self, instance):
        self._update_velocity()
        self._change_position()
        self._reset_acceleration()

    def _change_position(self):
        self.x += self.velocity_x
        if self.velocity_x:
            self.dispatch("on_move_x")
        self.y += self.velocity_y
        if self.velocity_y:
            self.dispatch("on_move_y")
        if self.velocity_y or self.velocity_x:
            self.dispatch("on_move")

    def _reset_acceleration(self):
        self.acceleration_x = self.acceleration_y = 0

    def move_stop_x(self):
        self.velocity_x = 0

    def move_stop_y(self):
        self.velocity_y = 0

    def move_stop(self):
        self.move_stop_x()
        self.move_stop_y()

    def on_velocity_x(self, instance, value):
        if not value and self.in_move:
            self.dispatch("on_stop_x")
            if not self.velocity_y:
                self.dispatch("on_stop")

    def on_velocity_y(self, instance, value):
        if not value and self.in_move:
            self.dispatch("on_stop_y")
            if not self.velocity_x:
                self.dispatch("on_stop")

    def on_move(self):
        self.in_move = True

    def on_move_x(self):
        pass

    def on_move_y(self):
        pass

    def on_stop(self):
        self.in_move = False

    def on_stop_x(self):
        pass

    def on_stop_y(self):
        pass
