from kivy.properties import ObjectProperty
from kivy.resources import resource_find

from warlocks_war.objects.world_object import WorldObject


class ForegroundImageNotFound(Exception):
    pass


class ImageView(WorldObject):

    foreground = ObjectProperty(None)

    def __init__(self, *args, foreground=None, foreground_pos=None, foreground_size=None, **kwargs):
        if foreground is None or not resource_find(foreground):
            raise ForegroundImageNotFound("Foreground image not found: '%s'" % foreground)
        self.foreground = foreground
        super(ImageView, self).__init__(*args, **kwargs)
