from warlocks_war.objects.behaviour_mixins import Movable, ImageView
from warlocks_war.objects.world_object import WorldObject


class Actor(Movable, ImageView, WorldObject):
    pass
