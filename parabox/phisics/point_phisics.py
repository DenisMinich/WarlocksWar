from kivy.vector import Vector

from parabox.phisics.base_phisics import BasePhisics


class PointPhisics(BasePhisics):

    def __init__(self, *args, gravity=0, affect_radius=0, **kwargs):
        super(PointPhisics, self). __init__(*args, **kwargs)
        self.gravity = gravity
        self.affect_radius = affect_radius

    def _get_acceleration(self, world_object):
        acceleration_vector = Vector(self.x - world_object.x, self.y - world_object.y)
        if self.affect_radius < acceleration_vector.length():
            acceleration_vector *= 0
        else:
            acceleration_vector *= (1 - acceleration_vector.length() / self.affect_radius) * self.gravity
        return acceleration_vector
