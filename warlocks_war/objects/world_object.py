from kivy.uix.widget import Widget

from warlocks_war.objects.collector import Collector


class WorldObject(Widget):
    def __init__(self, *args, **kwargs):
        super(WorldObject, self).__init__(*args, **kwargs)
        self.register_event_type("on_update")
        Collector.add_to_collection(self, "world_objects")

    def update(self):
        self.dispatch("on_update")

    def on_update(self):
        pass

    def _get_relative_coords_by_absolute(self, x, y):
        return x - self.pos[0], y - self.pos[1]

    def _get_absolute_coords_by_relative(self, x, y):
        return x + self.pos[0], y + self.pos[1]
