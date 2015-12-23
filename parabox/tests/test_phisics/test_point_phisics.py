import testscenarios
import unittest
from kivy.vector import Vector

from parabox.behaviour import Movable
from parabox.phisics import PointPhisics
from parabox.structures import Collector


class TestPointPhisics(testscenarios.TestWithScenarios):
    def setUp(self):
        self.point = PointPhisics(
            gravity=1,
            affect_radius=100,
            pos=(100, 100),
            affect_objects=Collector.get_collection('base_objects'))

    scenarios= [
        ('Out of range', dict(pos=(200, 100), acc=(0, 0))),
        ('In range', dict(pos=(50, 50), acc=(14.6446609, 14.6446609))),
    ]

    def test_acceleration(self):
        affected = Movable(pos=self.pos)
        self.assertEqual(affected.acceleration, Vector(0, 0))
        self.point.update()
        self.assertAlmostEqual(affected.acceleration[0], self.acc[0])
        self.assertAlmostEqual(affected.acceleration[1], self.acc[1])
