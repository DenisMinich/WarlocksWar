import mock
import unittest

from parabox.base_object import BaseObject


class TestBaseObject(unittest.TestCase):
    def setUp(self):
        self.object_example = BaseObject(
            angle=45,
            size=(25, 50),
            pos=(100, 100))

    def test_relative_to_absolute(self):
        self.assertEqual(
            self.object_example._get_relative_coords_by_absolute(
                110, 120),
            (10, 20))

    def test_absolute_to_relative(self):
        self.assertEqual(
            self.object_example._get_absolute_coords_by_relative(
                20, 30),
            (120, 130))

    def test_update_method(self):
        m = mock.Mock()
        self.object_example.bind(on_update=m.some_method)
        self.object_example.update()
        self.assertEqual(m.some_method.call_count, 1)

    def test_on_angle(self):
        m = mock.Mock()
        self.object_example.bind(on_rotate=m.some_method)
        self.object_example.angle = 55
        self.assertEqual(m.some_method.call_count, 1)
        self.assertEqual(
            m.some_method.call_args[0], (mock.ANY, 55, 10))
        self.object_example.angle = 50
        self.assertEqual(m.some_method.call_count, 2)
        self.assertEqual(
            m.some_method.call_args[0], (mock.ANY, 50, -5))
