from kivy.uix.widget import Widget
from kivy.vector import Vector


class WorldObject(Widget):
    def __init__(self, *args, foreground_image=None, **kwargs):
        super(WorldObject, self).__init__(*args, **kwargs)
        self.foreground_image = foreground_image
        self.register_event_type("on_update")

    def update(self):
        self.dispatch("on_update")

    def on_update(self):
        pass

    def get_resistance_vector(self, widget):
        self_left_edge_x, self_right_edge_x = self.pos[0], self.pos[0] + self.size[0]
        self_bottom_edge_y, self_top_edge_y = self.pos[1], self.pos[1] + self.size[1]
        widget_left_edge_x, widget_right_edge_x = widget.pos[0], widget.pos[0] + widget.size[0]
        widget_bottom_edge_y, widget_top_edge_y = widget.pos[1], widget.pos[1] + widget.size[1]
        if widget_left_edge_x < self_left_edge_x and widget_right_edge_x >= self_left_edge_x:
            return Vector(-1, 0)
        if widget_left_edge_x <= self_right_edge_x and widget_right_edge_x > self_right_edge_x:
            return Vector(1, 0)
        if widget_bottom_edge_y < self_bottom_edge_y and widget_top_edge_y >= self_bottom_edge_y:
            return Vector(0, -1)
        if widget_bottom_edge_y <= self_top_edge_y and widget_top_edge_y > self_top_edge_y:
            return Vector(0, 1)
        return None

    def _get_relative_coords_by_absolute(self, x, y):
        return x - self.pos[0], y - self.pos[1]

    def _get_absolute_coords_by_relative(self, x, y):
        return x + self.pos[0], y + self.pos[1]
