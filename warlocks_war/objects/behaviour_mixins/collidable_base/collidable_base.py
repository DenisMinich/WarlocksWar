from kivy.vector import Vector

from warlocks_war.objects.world_object import WorldObject


class CollidableBase(WorldObject):
    def __init__(self, *args, resistance_vector=(0, 0), **kwargs):
        super(CollidableBase, self).__init__(*args, **kwargs)
        self.resistance_vector = Vector(resistance_vector)
        self.add_to_collections(["collidable"])

    def get_resistance_vector(self, widget):
        return self.resistance_vector
