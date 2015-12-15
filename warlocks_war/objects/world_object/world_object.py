from kivy.properties import NumericProperty
from kivy.uix.widget import Widget

from warlocks_war.objects.collector import Collectable


class WorldObject(Widget, Collectable):

    angle = NumericProperty(0)

    def __init__(self, *args, **kwargs):
        super(WorldObject, self).__init__(*args, **kwargs)
        self.register_event_type("on_update")
        self.add_to_collections(["world_objects"])

    def update(self, *args, **kwargs):
        self.dispatch("on_update")

    def on_update(self):
        pass

    def _get_relative_coords_by_absolute(self, x, y):
        return x - self.pos[0], y - self.pos[1]

    def _get_absolute_coords_by_relative(self, x, y):
        return x + self.pos[0], y + self.pos[1]