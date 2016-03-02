from functools import partial

from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from parabox.structures import Collectable


class BaseObject(Widget, Collectable):
    """Base class for all parabox behaviour and phisics entities."""

    angle = NumericProperty(0)

    _old_angle = NumericProperty(0)

    def __init__(self, *args, angle=0, **kwargs):
        """BaseObject contructor"""
        super(BaseObject, self).__init__(*args, **kwargs)
        self.angle = angle
        self.register_event_type("on_update")
        self.register_event_type("on_rotate")
        self.bind(angle=self._dispatch_on_rotate)
        self.add_to_collections(["base_objects"])
        self._old_angle = self.angle
        self._planed_actions = []
        self.bind(on_update=self._call_planed_actions)

    def update(self, *args, **kwargs):
        """Update entity method.

        Dispatches 'on_update' event, which used in child classes.

        .. note:: Shouldn't be overwrited in child classes.
        """
        self.dispatch("on_update")

    def on_update(self):
        """Update entity event"""
        pass

    def on_rotate(self, new_value, diff):
        """Extended event on angle change with diffinition arg

        :param instance: Event object instance
        :type instance: BaseObject
        :param new_value: New angle value
        :type new_value: int
        :param diff: Difference between new and old values
        :type diff: int
        """
        pass

    def plan_action(self, ticks_count, action, *args, **kwargs):
        """Bind call action after some tick counts

        :param ticks_count: ticks count to wait
        :type ticks_count: int
        :param action: action to call
        :type action: function
        :param args: args to call action with
        :type args: list
        :param kwargs: keyword args to call action with
        :type kwargs: dict
        """
        self._planed_actions.append({
            'ticks': ticks_count,
            'action': partial(action, *args, **kwargs)})

    def _call_planed_actions(self, instance):
        """Reduce ticks counts in _planed_actions and call actions

        :param instance: Event object instance
        :type instance: BaseObject
        """
        for action in self._planed_actions:
            action['ticks'] -= 1
            if not action['ticks']:
                action['action']()
                self._planed_actions.remove(action)

    def _dispatch_on_rotate(self, instance, new_value):
        """Calculate new and old angle difference and dispatch on_rotate

        :param instance: Event object instance
        :type instance: BaseObject
        :param new_value: New angle value
        :type new_value: int
        """
        self.dispatch(
            'on_rotate', new_value, new_value-self._old_angle)
        self._old_angle = self.angle

    def _get_relative_coords_by_absolute(self, x, y):
        """Return widget's relative coords by absolute

        :param x: absolute x coord
        :type x: float
        :param y: absolute y coord
        :type y: float
        :returns: widget's relative coords
        :rtype: set of float
        """
        return x - self.pos[0], y - self.pos[1]

    def _get_absolute_coords_by_relative(self, x, y):
        """Return widget's absolute coords by relative

        :param x: relative x coord
        :type x: float
        :param y: relative y coord
        :type y: float
        :returns: widget's absolute coords
        :rtype: set of float
        """
        return x + self.pos[0], y + self.pos[1]
