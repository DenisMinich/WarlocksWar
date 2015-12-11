from math import sin, cos, pi

from kivy.vector import Vector
from numpy import array, zeros

from warlocks_war.objects.collector import Collector
from warlocks_war.objects.world_object import WorldObject


class Collidable(WorldObject):
    def __init__(self, *args, **kwargs):
        super(Collidable, self).__init__(*args, **kwargs)
        self.add_to_collections(["collidable"])
        self.bind(on_update=self.process_collisions)

    def process_collisions(self, instance):
        for widget in Collector.get_collection("collidable"):
            if self is not widget and self.collide_widget(widget) and widget.collide_widget(self):
                base, additional = (widget, self) if self.static else (self, widget)
                base.velocity, additional.velocity = Collidable.get_velocity_after_collission(
                    base, additional)
                while self.collide_widget(widget) and widget.collide_widget(self):
                    if not self.static:
                        self.move(self)
                    if not widget.static:
                        widget.move(widget)

    @staticmethod
    def get_intersection(first, second):
        if second.size < first.size:
            first, second = second, first
        intersection = array([[0, 0], [0, 0]], dtype=int)
        have_intersection = False
        for x, y in first.get_collide_check_pixels():
            world_x, world_y = first._get_absolute_coords_by_relative(x, y)
            if second.collide_point(world_x, world_y) and first.collide_point(world_x, world_y):
                have_intersection = True
                if intersection[0, 0] == 0 or intersection[0, 0] > world_x:
                    intersection[0, 0] = world_x
                if intersection[1, 0] == 0 or intersection[1, 0] < world_x:
                    intersection[1, 0] = world_x
                if intersection[0, 1] == 0 or intersection[0, 1] > world_y:
                    intersection[0, 1] = world_y
                if intersection[1, 1] == 0 or intersection[1, 1] < world_y:
                    intersection[1, 1] = world_y
        return intersection if have_intersection else None

    def _get_affection_zone(self, intersection, expand=5):
        intersection_size = (
            intersection[1, 0] - intersection[0, 0] + 1,
            intersection[1, 1] - intersection[0, 1] + 1)
        affection_zone = zeros([
                intersection_size[0] + expand * 2,
                intersection_size[1] + expand * 2,],
            dtype=bool)
        for x in range(intersection[0, 0] - expand, intersection[1, 0] + expand + 1):
            for y in range(intersection[0, 1] - expand, intersection[1, 1] + expand + 1):
                if self.collide_point(x, y):
                    local_x = x - intersection[0, 0] + expand
                    local_y = y - intersection[0, 1] + expand
                    affection_zone[local_x, local_y] = True
        return affection_zone

    def _calculate_resistance_vector(self, affection_zone):
        resistance_vector = Vector(0, 0)
        for x in range(affection_zone.shape[0]):
            for y in range(affection_zone.shape[1]):
                if not affection_zone[x, y]:
                    resistance_vector += Vector(
                        x - affection_zone.shape[0] // 2,
                        y - affection_zone.shape[1] // 2).normalize()
        return resistance_vector.normalize()

    def get_collide_check_pixels(self):
        check_pixels = []
        for x in range(self.size[0] + 1):
            if x == 0 or x == self.size[0]:
                y_values_to_check = range(self.size[1] + 1)
            else:
                y_values_to_check = (0, self.size[1])
            for y in y_values_to_check:
                check_pixels.append((x, y))
        return check_pixels

