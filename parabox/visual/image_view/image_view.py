from kivy.properties import ObjectProperty
from kivy.resources import resource_find

from parabox.base_object import BaseObject


class ForegroundImageNotFound(Exception):
    pass


class ImageView(BaseObject):
    """Mixin for image foreground"""

    foreground = ObjectProperty(None)

    def __init__(self, *args, foreground=None, **kwargs):
        """ImageView constructor

        :param foreground: path to foreground image
        :type foreground: str
        :raises: ForegroundImageNotFound
        """
        if foreground is None or not resource_find(foreground):
            raise ForegroundImageNotFound(
                "Foreground image not found: '%s'" % foreground)
        self.foreground = foreground
        super(ImageView, self).__init__(*args, **kwargs)
