from kivy.vector import Vector

from warlocks_war.phisics.model_types.base_phisics import BasePhisics


class PointPhisics(BasePhisics):

    def __init__(self, *args, gravity=0, coords=(0, 0), affection_radius=0, **kwargs):
        super(PointPhisics, self). __init__(*args, **kwargs)
        self.gravity = gravity
        self.coords = Vector(coords)
        self.affection_radius = affection_radius

    def _get_acceleration(self, world_object):
        acceleration_vector = Vector(self.coords.x - world_object.x, self.coords.y - world_object.y)
        if self.affection_radius < acceleration_vector.length():
            acceleration_vector *= 0
        else:
            acceleration_vector *= (1 - acceleration_vector.length() / self.affection_radius) * self.gravity
        return acceleration_vector
