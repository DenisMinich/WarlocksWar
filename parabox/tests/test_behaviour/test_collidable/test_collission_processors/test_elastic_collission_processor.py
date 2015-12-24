from kivy.vector import Vector
import testscenarios

from parabox.behaviour import Collidable
from parabox.behaviour.collidable.collission_processors import (
    ElasticCollissionProcessor)
from parabox.behaviour import Movable


class CollidableMovable(Collidable, Movable):
    pass


class TestProcessCollission(testscenarios.TestWithScenarios):
    def setUp(self):
        self.first = CollidableMovable(
            size=(3, 3), pos=(5, 1), velocity=(-1, -1))
        self.second = CollidableMovable(size=(5, 5))

    scenarios = [
        ('Small and Wall', dict(
            second_mass=None,
            first_result_velocity=Vector(1, -1),
            second_result_velocity=Vector(0, 0))),
        ('Small and Small', dict(
            second_mass=1,
            first_result_velocity=Vector(0, -1),
            second_result_velocity=Vector(-1, 0))),
        ('Small and Big', dict(
            second_mass=3,
            first_result_velocity=Vector(.5, -1),
            second_result_velocity=Vector(-.5, 0))),
    ]

    def test_get_collission_vector(self):
        self.second.mass = self.second_mass
        ElasticCollissionProcessor.process_collission(self.first, self.second)
        self.assertAlmostEqual(
            self.first.velocity[0], self.first_result_velocity.x)
        self.assertAlmostEqual(
            self.first.velocity[1], self.first_result_velocity.y)
        self.assertAlmostEqual(
            self.second.velocity[0], self.second_result_velocity.x)
        self.assertAlmostEqual(
            self.second.velocity[1], self.second_result_velocity.y)
