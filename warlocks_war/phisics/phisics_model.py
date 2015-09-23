from kivy.vector import Vector


class PhisicsModel(list):

    def __init__(self, *args, speed_limit=10.):
        super(PhisicsModel, self).__init__(args)
        self.speed_limit = speed_limit

    def _get_acceleration(self, world_object):
        acceleration = Vector(0, 0)
        for phisics_object in self:
            acceleration += phisics_object.get_acceleration(world_object)
        return acceleration

    def _update_velocity(self, world_object, acceleration):
        world_object.velocity = Vector(*world_object.velocity) + Vector(*acceleration)
        velocity_vector = Vector(world_object.velocity)
        if velocity_vector.length() > self.speed_limit:
            world_object.velocity = velocity_vector * self.speed_limit / velocity_vector.length()

    def process(self, world_objects):
        for world_object in world_objects:
            acceleration = self._get_acceleration(world_object)
            self._update_velocity(world_object, acceleration)
            world_object.move()
