from mock import Mock
import unittest

from parabox.behaviour import Movable


class TestMovable(unittest.TestCase):
    def setUp(self):
        self.in_move = Movable(velocity=(1, 1))
        self.in_move.in_move = True
        self.stoped = Movable(velocity=(0, 0))

    def test_in_move(self):
        self.in_move.mock = Mock()
        self.in_move.bind(on_move=self.in_move.mock.on_move)
        self.in_move.bind(on_move_x=self.in_move.mock.on_move_x)
        self.in_move.bind(on_move_y=self.in_move.mock.on_move_y)
        self.in_move.bind(on_stop=self.in_move.mock.on_stop)
        self.in_move.bind(on_stop_x=self.in_move.mock.on_stop_x)
        self.in_move.bind(on_stop_y=self.in_move.mock.on_stop_y)
        self.assertEqual(self.in_move.acceleration, [0, 0])
        self.in_move.acceleration = (-1, -1)
        self.in_move.update()
        self.assertEqual(self.in_move.acceleration, [0, 0])
        self.assertEqual(self.in_move.velocity, [0, 0])
        self.assertEqual(self.in_move.pos, [0, 0])
        self.assertEqual(self.in_move.mock.on_move.call_count, 0)
        self.assertEqual(self.in_move.mock.on_move_x.call_count, 0)
        self.assertEqual(self.in_move.mock.on_move_y.call_count, 0)
        self.assertEqual(self.in_move.mock.on_stop.call_count, 1)
        self.assertEqual(self.in_move.mock.on_stop_x.call_count, 1)
        self.assertEqual(self.in_move.mock.on_stop_y.call_count, 1)

    def test_stoped(self):
        self.stoped.mock = Mock()
        self.stoped.bind(on_move=self.stoped.mock.on_move)
        self.stoped.bind(on_move_x=self.stoped.mock.on_move_x)
        self.stoped.bind(on_move_y=self.stoped.mock.on_move_y)
        self.stoped.bind(on_stop=self.stoped.mock.on_stop)
        self.stoped.bind(on_stop_x=self.stoped.mock.on_stop_x)
        self.stoped.bind(on_stop_y=self.stoped.mock.on_stop_y)
        self.assertEqual(self.stoped.acceleration, [0, 0])
        self.stoped.acceleration = (1, 1)
        self.stoped.update()
        self.assertEqual(self.stoped.acceleration, [0, 0])
        self.assertEqual(self.stoped.velocity, [1, 1])
        self.assertEqual(self.stoped.pos, [1, 1])
        self.assertEqual(self.stoped.mock.on_move.call_count, 1)
        self.assertEqual(self.stoped.mock.on_move_x.call_count, 1)
        self.assertEqual(self.stoped.mock.on_move_y.call_count, 1)
        self.assertEqual(self.stoped.mock.on_stop.call_count, 0)
        self.assertEqual(self.stoped.mock.on_stop_x.call_count, 0)
        self.assertEqual(self.stoped.mock.on_stop_y.call_count, 0)
