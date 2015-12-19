from kivy.vector import Vector

from parabox.phisics.base_phisics import BasePhisics


class PlainPhisics(BasePhisics):
    """Phisics model with linear gravity vector"""

    def __init__(self, *args, gravity=(0, 0), **kwargs):
        """PlainPisics constructor

        :param gravity: gravity vector
        :param gravity: kivy.Vector
        """
        super(PlainPhisics, self). __init__(*args, **kwargs)
        self.gravity = Vector(gravity)

    def _get_acceleration(self, world_object):
        """Returns object's acceleration change

        :param world_object: object which acceleration will be changed
        :type world_object: parabox.base_object.BaseObject
        """
        return self.gravity.rotate(self.angle)
