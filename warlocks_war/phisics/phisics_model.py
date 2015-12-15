from kivy.vector import Vector


class PhisicsModel(list):

    def __init__(self, *args, **kwargs):
        super(PhisicsModel, self).__init__(args)
        self.pos = self.parent.pos

    def _get_acceleration(self, world_object):
        acceleration = Vector(0, 0)
        for phisics_object in self:
            acceleration += phisics_object.get_acceleration(world_object)
        return acceleration

    def process(self, world_objects):
        for world_object in world_objects:
            acceleration = self._get_acceleration(world_object)
            world_object.acceleration = Vector(acceleration)
