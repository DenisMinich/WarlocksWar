from kivy.vector import Vector


class PlainPhisics(object):

    def __init__(self, gravity=(0, 0)):
        super(PlainPhisics, self). __init__()
        self.gravity = Vector(gravity)

    def get_acceleration(self, world_object):
        return self.gravity
