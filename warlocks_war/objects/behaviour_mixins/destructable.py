from kivy.vector import Vector
from numpy import ones

from warlocks_war.objects.world_object import WorldObject


class Destructable(WorldObject):
    def __init__(self, *args, bitmap=None, **kwargs):
        super(Destructable, self).__init__(*args, **kwargs)
        self.bitmap = ones(self.size, dtype=bool) if bitmap is None else bitmap

    def collide_point(self, x, y):
        if super(Destructable, self).collide_point(x, y):
            return self.bitmap[self._get_relative_coords_by_absolute(x, y)]
        return False

    def _get_relative_coords_by_absolute(self, x, y):
        return tuple(Vector(x, y) - Vector(self.pos))
