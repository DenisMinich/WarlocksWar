from kivy.vector import Vector

from warlocks_war.objects import WorldObject
from warlocks_war.objects.collector import Collector


class BasePhisics(WorldObject):

    def __init__(self, *args, affect_objects=None, **kwargs):
        super(BasePhisics, self).__init__(*args, **kwargs)
        self.affect_objects = [] if affect_objects is None else affect_objects
        self.add_to_collections(["world_phisics"])

    def _get_acceleration(self, world_object):
        return Vector(0, 0)

    def update(self, *args, **kwargs):
        print('Affect objects', self.affect_objects)
        for affect_object in self.affect_objects:
            if affect_object in Collector.get_collection('movable'):
                affect_object.acceleration = (
                    Vector(affect_object.acceleration) + self._get_acceleration(affect_object))
