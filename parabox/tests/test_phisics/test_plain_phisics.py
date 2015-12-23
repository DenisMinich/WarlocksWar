from kivy.vector import Vector
import unittest

from parabox.behaviour import Movable
from parabox.phisics import PlainPhisics


class TestPlainPhisics(unittest.TestCase):
    def setUp(self):
        self.affected = Movable()
        self.down = PlainPhisics(
            gravity=(0, -1), affect_objects=[self.affected])
        self.right = PlainPhisics(
            gravity=(0, 2), affect_objects=[self.affected], angle=-90)

    def test_acceleration(self):
        self.assertEqual(self.affected.acceleration, Vector(0, 0))
        self.down.update()
        self.right.update()
        self.assertAlmostEqual(self.affected.acceleration[0], 2)
        self.assertAlmostEqual(self.affected.acceleration[1], -1)
