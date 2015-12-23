import os

import numpy
import unittest

from parabox.behaviour import Bitmap


class TestBitmap(unittest.TestCase):
    def setUp(self):
        self.filename = 'temp_bitmap.csv'
        with open(self.filename, 'w+') as file:
            file.write(''.join([
                "     0,    0,    0,    0,    1\n",
                "     0,    0,    0,    1,    1\n",
                "     0,    0,    1,    1,    1\n",
                "     0,    1,    1,    1,    1\n",
                "     1,    1,    1,    1,    1\n"]))

    def tearDown(self):
        os.remove(self.filename)

    def test_default_bitmap(self):
        bitmap = Bitmap(size=(4, 4))
        self.assertTrue(
            (bitmap.bitmap == numpy.ones((4, 4), dtype=bool)).all())

    def test_resize_bitmap(self):
        first = Bitmap(size=(3, 3), bitmap=self.filename)
        self.assertTrue((first.bitmap == numpy.array(
            [[True, True, True],
             [False, True, True],
             [False, False, True]],
            dtype=bool)).all())
        first = Bitmap(size=(7, 7), bitmap=self.filename)
        self.assertTrue((first.bitmap == numpy.array(
            [[True, True, True, True, True, True, True],
             [True, True, True, True, True, True, True],
             [False, False, True, True, True, True, True],
             [False, False, False, True, True, True, True],
             [False, False, False, True, True, True, True],
             [False, False, False, False, False, True, True],
             [False, False, False, False, False, False, True]],
            dtype=bool)).all())
