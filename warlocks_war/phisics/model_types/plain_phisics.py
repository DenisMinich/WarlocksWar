from kivy.vector import Vector

from warlocks_war.phisics.model_types.base_phisics import BasePhisics


class PlainPhisics(BasePhisics):

    def __init__(self, *args, gravity=(0, 0), **kwargs):
        super(PlainPhisics, self). __init__(*args, **kwargs)
        self.gravity = Vector(gravity)

    def _get_acceleration(self, world_object):
        return self.gravity
