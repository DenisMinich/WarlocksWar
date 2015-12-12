from kivy.vector import Vector

from warlocks_war.objects.behaviour_mixins.collidable.collission_processors import (
    ElasticCollissionProcessor)
from warlocks_war.objects.behaviour_mixins import (
    Movable, ImageView, Collidable)
from warlocks_war.objects.world_object import WorldObject
from warlocks_war.objects.structures import WidgetsCollection
from warlocks_war.phisics import PlainPhisics


class Actor(Movable, Collidable, ImageView, WorldObject):
    def __init__(self, *args, **kwargs):
        super(Actor, self).__init__(*args, **kwargs)
        self.own_gravity = PlainPhisics(gravity=(0, .001), affect_objects=[self]) 
        self.phisics = WidgetsCollection([self.own_gravity], self)
        self.bind(on_collide=ElasticCollissionProcessor.process_collission)
        self.bind(on_update=self.change_inner_phisic)

    def change_inner_phisic(self, *args, **kwargs):
        self.own_gravity.gravity += Vector(0, .002)

