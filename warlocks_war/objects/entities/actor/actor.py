from warlocks_war.objects.behaviour_mixins.collidable.collission_processors import (
    ElasticCollissionProcessor)
from warlocks_war.objects.behaviour_mixins import (
    Movable, ImageView, Collidable)
from warlocks_war.objects.world_object import WorldObject


class Actor(Movable, Collidable, ImageView, WorldObject):
    def __init__(self, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.bind(on_collide=ElasticCollissionProcessor.process_collission)
