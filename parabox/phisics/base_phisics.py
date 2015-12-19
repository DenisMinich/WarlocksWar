from kivy.vector import Vector

from parabox.base_object import BaseObject
from parabox.structures import Collector


class BasePhisics(BaseObject):
    """Base class for phisics generators"""

    def __init__(self, *args, affect_objects=None, **kwargs):
        """Base phisics contructor

        :param affect_objects: object which will be affected by this phisics
        :type affect_objects: iterable or None
        """
        super(BasePhisics, self).__init__(*args, **kwargs)
        self.affect_objects = [] if affect_objects is None else affect_objects
        self.add_to_collections(["world_phisics"])

    def _get_acceleration(self, world_object):
        """Returns object's acceleration change

        :param world_object: object which acceleration will be changed
        :type world_object: parabox.base_object.BaseObject
        """
        return Vector(0, 0)

    def update(self, *args, **kwargs):
        """Change affected objects' accelerations"""
        for affect_object in self.affect_objects:
            if affect_object in Collector.get_collection('movable'):
                affect_object.acceleration = (
                    Vector(affect_object.acceleration) +
                    self._get_acceleration(affect_object))
