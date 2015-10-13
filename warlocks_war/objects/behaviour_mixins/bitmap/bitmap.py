from numpy import ones, genfromtxt

from warlocks_war.objects.world_object import WorldObject

COLLIDE_MATRIX_SIZE = 5


class Bitmap(WorldObject):
    def __init__(self, *args, bitmap=None, **kwargs):
        super(Bitmap, self).__init__(*args, **kwargs)
        self.bitmap = self._get_bitmap(bitmap)

    def _get_bitmap(self, bitmap):
        if bitmap is not None:
            bitmap = genfromtxt(bitmap, delimiter=',', defaultfmt="%5i")
            bitmap = self._adapt_bitmap_to_widget_size(bitmap)
            return bitmap.astype(bool)
        return ones(self.size, dtype=bool)

    def _get_bitmap_coords_by_relative(self, relative_x, relative_y):
        relative_y = self.size[1] - relative_y - 1
        bitmap_x = relative_x * self.bitmap.shape[1] // self.size[0]
        bitmap_y = relative_y * self.bitmap.shape[0] // self.size[1]
        return bitmap_x, bitmap_y

    def _adapt_bitmap_to_widget_size(self, bitmap):
        return bitmap
