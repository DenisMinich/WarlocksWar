from kivy.vector import Vector

from warlocks_war.objects.collector import Collectable


class BasePhisics(Collectable):

    def __init__(self, *args, **kwargs):
        super(BasePhisics, self).__init__(*args, **kwargs)
        self.add_to_collections(["world_phisics"])

    def get_acceleration(self, world_object):
        return Vector(0, 0)
