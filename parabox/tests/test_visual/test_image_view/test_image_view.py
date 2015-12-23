import unittest

from parabox.visual.image_view.image_view import ForegroundImageNotFound
from parabox.visual.image_view.image_view import ImageView


class TestImageView(unittest.TestCase):
    def test_raise_no_image_found(self):
        self.assertRaises(ForegroundImageNotFound, ImageView)
