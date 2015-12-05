from decimal import Decimal
from functools import partial

from numpy import ones, genfromtxt, array, reshape

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

    def _adapt_bitmap_to_widget_size(self, bitmap):
        return self._transform_matrix(bitmap, self.size)

    def _transform_matrix(self, matrix, new_size):
        result = list()
        self._list_walker(
            array=matrix,
            size=new_size[0],
            func=partial(self._list_walker, size=new_size[1], func=result.append))
        return reshape(result, new_size)

    def _list_walker(self, array=None, size=None, func=None):
        ratio = Decimal(len(array)) / Decimal(size)
        current_fill_mark = 0
        for element in array:
            while current_fill_mark < 1:
                func(element)
                current_fill_mark += ratio
            if current_fill_mark >= 1:
                current_fill_mark -= 1

