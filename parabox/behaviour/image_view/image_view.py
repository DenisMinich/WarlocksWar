from kivy.properties import ObjectProperty
from kivy.resources import resource_find

from parabox.base_object import BaseObject


class ForegroundImageNotFound(Exception):
    pass


class ImageView(BaseObject):

    foreground = ObjectProperty(None)

    def __init__(self, *args, foreground=None, **kwargs):
        if foreground is None or not resource_find(foreground):
            raise ForegroundImageNotFound(
                "Foreground image not found: '%s'" % foreground)
        self.foreground = foreground
        super(ImageView, self).__init__(*args, **kwargs)
