from kivy.properties import (
    NumericProperty, ReferenceListProperty, BooleanProperty)
from kivy.vector import Vector

from parabox.base_object import BaseObject


class Movable(BaseObject):
    """Mixins for movable classes"""
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    acceleration_x = NumericProperty(0)
    acceleration_y = NumericProperty(0)
    acceleration = ReferenceListProperty(acceleration_x, acceleration_y)
    in_move = BooleanProperty(False)

    def __init__(
            self, *args, velocity=(0, 0), speed_limit=None,
            speed_limit_x=None, speed_limit_y=None,
            resistance_x=None, resistance_y=None, **kwargs):
        """Movable constructor

        :param velocity: velocity vector
        :type velocity: kivy.vector.Vector
        :param speed_limit: speed limit for object.
        :param speed_limit_x: speed limit by x coord.
        :param speed_limit_y: speed limit by y coord.
        :type speed_limit: float
        """
        super(Movable, self).__init__(*args, **kwargs)
        self.speed_limit = speed_limit
        self.speed_limit_x = speed_limit_x
        self.speed_limit_y = speed_limit_y
        self.resistance_x = resistance_x
        self.resistance_y = resistance_y
        self.velocity = velocity
        self.in_move = True if velocity[0] or velocity[1] else False
        self.add_to_collections(["movable"])
        self.register_event_type('on_move')
        self.register_event_type('on_move_x')
        self.register_event_type('on_move_y')
        self.register_event_type('on_stop')
        self.register_event_type('on_stop_x')
        self.register_event_type('on_stop_y')
        self.bind(on_update=self.move)

    def _update_velocity(self):
        """Change velocity because of acceleration"""
        self.velocity = Vector(*self.velocity) + Vector(*self.acceleration)
        self._apply_resistance()
        self._restrict_velocity()

    def _apply_resistance(self):
        """Apply movement resistance"""
        if self.resistance_x is not None:
            if self.velocity_x >= 0:
                if self.velocity_x < self.resistance_x:
                    self.velocity_x = 0
                else:
                    self.velocity_x -= self.resistance_x
            else:
                if self.velocity_x > -self.resistance_x:
                    self.velocity_x = 0
                else:
                    self.velocity_x += self.resistance_x
        if self.resistance_x is not None:
            if self.velocity_y >= 0:
                if self.velocity_y < self.resistance_x:
                    self.velocity_y = 0
                else:
                    self.velocity_y -= self.resistance_x
            else:
                if self.velocity_y > -self.resistance_x:
                    self.velocity_y = 0
                else:
                    self.velocity_y += self.resistance_x

    def _restrict_velocity(self):
        """Restrict velocity with speed limit"""
        if self.speed_limit_x is not None:
            if self.velocity_x > self.speed_limit_x:
                self.velocity_x = self.speed_limit_x
            if self.velocity_x < -self.speed_limit_x:
                self.velocity_x = -self.speed_limit_x
        if self.speed_limit_y is not None:
            if self.velocity_y > self.speed_limit_y:
                self.velocity_y = self.speed_limit_y
            if self.velocity_y < -self.speed_limit_y:
                self.velocity_y = -self.speed_limit_y
        if self.speed_limit is not None:
            velocity_vector = Vector(self.velocity)
            if velocity_vector.length() > self.speed_limit:
                self.velocity = (velocity_vector * self.speed_limit /
                                 velocity_vector.length())

    def move(self, instance):
        """Move object

        :param instance: self analog
        :type instance: kivy.uix.widget.Widget
        """
        self._update_velocity()
        self._change_position()
        self._reset_acceleration()

    def move_manual(self, velocity_x, velocity_y):
        """Move object with fixed velocity

        Dont trigger move/stop events
        :param velocity_x: velocity by x axis
        :type velocity_x: float
        :param velocity_y: velocity by y axis
        :type velocity_y: float
        """
        self.x += velocity_x
        self.y += velocity_y

    def _change_position(self):
        """Change objects position"""
        self.x += self.velocity_x
        if self.velocity_x:
            self.dispatch("on_move_x")
        self.y += self.velocity_y
        if self.velocity_y:
            self.dispatch("on_move_y")
        if self.velocity_y or self.velocity_x:
            self.dispatch("on_move")

    def _reset_acceleration(self):
        """Set acceleration to zero"""
        self.acceleration_x = self.acceleration_y = 0

    def move_stop_x(self):
        """Stop in x direction"""
        self.velocity_x = 0

    def move_stop_y(self):
        """Stop in y direction"""
        self.velocity_y = 0

    def move_stop(self):
        """Stop object"""
        self.move_stop_x()
        self.move_stop_y()

    def on_velocity_x(self, instance, value):
        """Dispatch event on x move"""
        if not value and self.in_move:
            self.dispatch("on_stop_x")
            if not self.velocity_y:
                self.dispatch("on_stop")

    def on_velocity_y(self, instance, value):
        """Dispatch event on y move"""
        if not value and self.in_move:
            self.dispatch("on_stop_y")
            if not self.velocity_x:
                self.dispatch("on_stop")

    def on_move(self):
        """On move event"""
        self.in_move = True

    def on_move_x(self):
        """On move x event"""
        pass

    def on_move_y(self):
        """On move y event"""
        pass

    def on_stop(self):
        """On stop event"""
        self.in_move = False

    def on_stop_x(self):
        """On stop x event"""
        pass

    def on_stop_y(self):
        """On stop y event"""
        pass
