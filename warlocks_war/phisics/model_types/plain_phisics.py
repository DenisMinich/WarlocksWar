from kivy.vector import Vector

from warlocks_war.phisics.model_types.base_phisics import BasePhisics


class PlainPhisics(BasePhisics):

    def __init__(self, gravity=(0, 0)):
        super(PlainPhisics, self). __init__()
        self.gravity = Vector(gravity)

    def get_acceleration(self, world_object):
        return self.gravity
