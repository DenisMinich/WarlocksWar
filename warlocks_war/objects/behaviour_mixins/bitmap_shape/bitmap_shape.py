import os.path

from kivy.vector import Vector
from numpy import array, ones, genfromtxt

from warlocks_war.objects.world_object import WorldObject
from warlocks_war.settings import STATIC_PATH

COLLIDE_MATRIX_SIZE = 5


class BitmapShape(WorldObject):
    def __init__(self, *args, bitmap=None, **kwargs):
        super(BitmapShape, self).__init__(*args, **kwargs)
        self.bitmap = self._get_bitmap(bitmap)

    def _get_bitmap(self, bitmap):
        if bitmap is not None:
            return bitmap
        if self.foreground is None:
            return ones(self.size, dtype=bool)
        bitmap_path = os.path.join(STATIC_PATH, "{}.csv".format(self.foreground[:-4]))
        if os.path.isfile(bitmap_path):
            bitmap = genfromtxt(bitmap_path, delimiter=',', defaultfmt="%5i")
            return bitmap.astype(bool)
        return ones(self.size, dtype=bool)

    def collide_widget(self, widget):
        if super(BitmapShape, self).collide_widget(widget):
            return bool(self._get_widgets_collide_point(widget))
        return False

    def collide_point(self, x, y):
        if super(BitmapShape, self).collide_point(x, y):
            relative_x, relative_y = self._get_relative_coords_by_absolute(x, y)
            bitmap_x, bitmap_y = self._get_bitmap_coords_by_relative(relative_x, relative_y)
            if 0 <= bitmap_x < self.bitmap.shape[1] and 0 <= bitmap_y < self.bitmap.shape[0]:
                return self.bitmap[bitmap_y, bitmap_x]
        return False

    def get_resistance_vector(self, widget):
        collide_point = self._get_widgets_collide_point(widget)
        if collide_point is not None:
            collide_matrix = self._get_collide_point_matrix(*collide_point)
            return self._calculate_resistance_vector(collide_matrix)
        return None

    def _get_bitmap_coords_by_relative(self, relative_x, relative_y):
        relative_y = self.size[1] - relative_y - 1
        bitmap_x = relative_x * self.bitmap.shape[1] // self.size[0]
        bitmap_y = relative_y * self.bitmap.shape[0] // self.size[1]
        return bitmap_x, bitmap_y

    def _get_widgets_collide_point(self, widget):
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                world_x, world_y = self._get_absolute_coords_by_relative(x, y)
                if self.collide_point(world_x, world_y) and widget.collide_point(world_x, world_y):
                    return world_x, world_y
        return None

    def _get_collide_point_matrix(self, collide_point_x, collide_point_y):
        y_range = range(collide_point_y - COLLIDE_MATRIX_SIZE // 2,
                        collide_point_y + COLLIDE_MATRIX_SIZE // 2 + 1)
        x_range = range(collide_point_x - COLLIDE_MATRIX_SIZE // 2,
                        collide_point_x + COLLIDE_MATRIX_SIZE // 2 + 1)
        return array([[self.collide_point(x, y) for x in x_range] for y in y_range], dtype=bool)

    def _calculate_resistance_vector(self, collide_matrix):
        resistance_vector = Vector(0, 0)
        for y_index in range(COLLIDE_MATRIX_SIZE):
            for x_index in range(COLLIDE_MATRIX_SIZE):
                if not collide_matrix[y_index, x_index]:
                    resistance_vector += Vector(
                        x_index - COLLIDE_MATRIX_SIZE // 2,
                        y_index - COLLIDE_MATRIX_SIZE // 2)
        return resistance_vector.normalize()
