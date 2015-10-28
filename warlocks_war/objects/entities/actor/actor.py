from warlocks_war.objects.behaviour_mixins import (
    Movable, ImageView, Collidable)
from warlocks_war.objects.world_object import WorldObject


class Actor(Movable, Collidable, ImageView, WorldObject):
    pass
