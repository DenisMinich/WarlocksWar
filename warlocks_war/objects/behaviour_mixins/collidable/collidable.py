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

    def get_resistance_vector(self, widget):
        intersection = self._get_intersection(widget)
        affection_zone = self._get_affection_zone(intersection)
        return self._calculate_resistance_vector(affection_zone)

    def process_collisions(self, instance):
        for widget in Collector.get_collection("collidable"):
            if self is not widget and self.collide_widget(widget):
                self.velocity, widget.velocity = Collidable.get_velocity_after_collission(
                    self, widget)
                while self.collide_widget(widget):
                    self.move(self)
                    widget.move(widget)

    @staticmethod
    def get_velocity_after_collission(first, second):
        collission_vector_x = second.get_resistance_vector(first)
        collission_vector_y = collission_vector_x.rotate(90)
        v1, v2 = first.velocity, second.velocity
        system_speed = Vector(v2)
        v1, v2 = Vector(v1) - system_speed, Vector(v2) - system_speed
        system_rotate_angle = Vector(1, 0).angle(collission_vector_x)
        v1a, v1b = Vector(v1).rotate(-system_rotate_angle)
        mass_ratio = 0 if not second.mass else first.mass / second.mass
        u1a_1, u1a_2 = Collidable.solve_quadratic_equation(
            a = mass_ratio + 1,
            b = -2 * mass_ratio * v1a,
            c = (mass_ratio - 1) * v1a ** 2)
        u1a = u1a_1 if u1a_1 != v1a else u1a_2
        u1b = v1b
        u2a = mass_ratio * (v1a - u1a)
        u2b = 0
        u1 = Vector(u1a, u1b).rotate(system_rotate_angle)
        u2 = Vector(u2a, u2b).rotate(system_rotate_angle)
        u1, u2 = u1 + system_speed, u2 + system_speed
        return u1, u2

    @staticmethod
    def solve_quadratic_equation(a, b, c):
        D = b ** 2 - 4 * a * c
        return (-b + D ** .5) / (2 * a), (-b - D ** .5) / (2 * a)

    def _get_intersection(self, widget):
        intersection = array([[0, 0], [0, 0]], dtype=int)
        have_intersection = False
        for x in range(self.size[0] + 1):
            for y in range(self.size[1] + 1):
                world_x, world_y = self._get_absolute_coords_by_relative(x, y)
                if widget.collide_point(world_x, world_y) and self.collide_point(world_x, world_y):
                    have_intersection = True
                    if intersection[0, 0] == 0:
                        intersection[0, 0] = world_x
                    intersection[1, 0] = world_x
                    if intersection[0, 1] == 0 or intersection[0, 1] > world_y:
                        intersection[0, 1] = world_y
                    if intersection[1, 1] == 0 or intersection[1, 1] < world_y:
                        intersection[1, 1] = world_y
        return intersection if have_intersection else None

    def _get_affection_zone(self, intersection, expand=1):
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

