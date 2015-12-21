from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from parabox.structures import Collectable


class BaseObject(Widget, Collectable):
    """
    Base class for all parabox behaviour and phisics entities.
    """

    angle = NumericProperty(0)

    def __init__(self, *args, angle=0, **kwargs):
        """
        BaseObject contructor
        """
        super(BaseObject, self).__init__(*args, **kwargs)
        self.angle = angle
        self.register_event_type("on_update")
        self.add_to_collections(["base_objects"])

    def update(self, *args, **kwargs):
        """
        Update entity method.
        Dispatches 'on_update' event, which used in child classes.

        .. note:: Shouldn't be overwrited in child classes.
        """
        self.dispatch("on_update")

    def on_update(self):
        """
        Update entity event
        """
        pass

    def _get_relative_coords_by_absolute(self, x, y):
        """
        Return widget's relative coords by absolute

        :param x: absolute x coord
        :type x: float
        :param y: absolute y coord
        :type y: float
        :returns: widget's relative coords
        :rtype: set of float
        """
        return x - self.pos[0], y - self.pos[1]

    def _get_absolute_coords_by_relative(self, x, y):
        """
        Return widget's absolute coords by relative

        :param x: relative x coord
        :type x: float
        :param y: relative y coord
        :type y: float
        :returns: widget's absolute coords
        :rtype: set of float
        """
        return x + self.pos[0], y + self.pos[1]
