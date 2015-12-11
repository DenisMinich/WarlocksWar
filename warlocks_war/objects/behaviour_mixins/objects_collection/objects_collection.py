from warlocks_war.objects.world_object import WorldObject
from warlocks_war.objects.behaviour_mixins.objects_collection.objects_model import ObjectsModel


class ObjectsCollection(WorldObject):
    def __init__(self, *args, inner_objects=None, **kwargs):
        super(ObjectsCollection, self).__init__(*args, **kwargs)
        self.inner_objects = ObjectsModel(
            [] if inner_objects is None else inner_objects,
            self)
        self.bind(on_update=self.inner_objects.update)

