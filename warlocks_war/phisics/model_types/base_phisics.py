from kivy.vector import Vector

from warlocks_war.objects.collector import Collector


class BasePhisics:

    def __init__(self, *args, **kwargs):
        super(BasePhisics, self).__init__(*args, **kwargs)
        Collector.add_to_collection(self, "world_phisics")

    def get_acceleration(self, world_object):
        return Vector(0, 0)
