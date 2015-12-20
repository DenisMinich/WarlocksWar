from kivy.vector import Vector

from parabox.phisics.base_phisics import BasePhisics


class PointPhisics(BasePhisics):
    """Phisics model with point direction"""

    def __init__(self, *args, gravity=0, affect_radius=0, **kwargs):
        """PlainPisics constructor

        :param gravity: gravity power
        :type gravity: float
        :param affect_radius: affect radius
        :type affect_radius: float
        """
        super(PointPhisics, self). __init__(*args, **kwargs)
        self.gravity = gravity
        self.affect_radius = affect_radius

    def _get_acceleration(self, world_object):
        """Returns object's acceleration change

        :param world_object: object which acceleration will be changed
        :type world_object: parabox.base_object.BaseObject
        :return: acceleration change
        :rtype: Vector
        """
        acceleration_vector = Vector(
            self.x - world_object.x, self.y - world_object.y)
        if self.affect_radius < acceleration_vector.length():
            acceleration_vector *= 0
        else:
            acceleration_vector *= (
                (1 - acceleration_vector.length() / self.affect_radius) *
                self.gravity)
        return acceleration_vector
