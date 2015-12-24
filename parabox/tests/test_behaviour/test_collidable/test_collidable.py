from kivy.vector import Vector
from mock import Mock
import testscenarios
import unittest

from parabox.base_object import BaseObject
from parabox.behaviour import Collidable


class TestCollissionVector(testscenarios.TestWithScenarios):
    def setUp(self):
        self.first = Collidable(size=(3, 3))
        self.second = Collidable(size=(5, 5))

    scenarios = [
        ('Top', dict(
            first_pos=(1, 5), resistance=Vector(0, 1))),
        ('Left', dict(
            first_pos=(5, 1), resistance=Vector(1, 0))),
        ('Corner', dict(
            first_pos=(5, 5), resistance=Vector(1, 1).normalize())),
    ]

    def test_get_collission_vector(self):
        self.first.pos = self.first_pos
        resistance = self.second.get_resistance_vector(self.first)
        self.assertAlmostEqual(resistance.x, self.resistance.x)
        self.assertAlmostEqual(resistance.y, self.resistance.y)


class TestCollidable(unittest.TestCase):
    def test_collide_dispatched(self):
        first = Collidable(size=(5, 5))
        first.mock = Mock()
        first.bind(on_collide=first.mock.some_method)

        second = Collidable(size=(5, 5), pos=(3, 3))
        second.mock = Mock()
        second.bind(on_collide=second.mock.some_method)

        third = Collidable(size=(5, 5), pos=(7, 7))
        third.mock = Mock()
        third.bind(on_collide=third.mock.some_method)

        fourth = Collidable(size=(5, 5), pos=(10, 0))
        fourth.mock = Mock()
        fourth.bind(on_collide=fourth.mock.some_method)

        fifth = BaseObject(size=(15, 15))

        first.update()
        second.update()
        third.update()
        fourth.update()
        fifth.update()

        self.assertEqual(first.mock.some_method.call_count, 1)
        self.assertEqual(second.mock.some_method.call_count, 2)
        self.assertEqual(third.mock.some_method.call_count, 1)
        self.assertEqual(fourth.mock.some_method.call_count, 0)
