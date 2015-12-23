from decimal import Decimal
from functools import partial

from numpy import ones, genfromtxt, reshape

from parabox.base_object import BaseObject


class Bitmap(BaseObject):
    """Associate object with bitmap mask"""

    def __init__(self, *args, bitmap=None, **kwargs):
        """Bitmap constructor

        :param bitmap: path to csv file
        :type bitmap: str
        """
        super(Bitmap, self).__init__(*args, **kwargs)
        self.bitmap = self._get_bitmap(bitmap)
        self.add_to_collections(["bitmap"])

    def _get_bitmap(self, bitmap):
        """Read csv file in memory

        :param bitmap: path to csv file
        :type bitmap: str
        :return: associated with object bitmap
        :rtype: binary matrix
        """
        if bitmap is not None:
            bitmap = genfromtxt(bitmap, delimiter=',', defaultfmt="%5i")
            bitmap = self._adapt_bitmap_to_widget_size(bitmap)
            return bitmap.astype(bool)
        return ones(self.size, dtype=bool)

    def _adapt_bitmap_to_widget_size(self, bitmap):
        """Read csv file in memory

        :param bitmap: path to csv file
        :type bitmap: str
        :return: associated with object bitmap
        :rtype: binary matrix
        """
        return self._transform_matrix(bitmap, self.size)

    def _transform_matrix(self, matrix, new_size):
        """Adobt bitmap to widget size

        :param matrix: bitmap with default size
        :type bitmap: binary matrix
        :param new_size: new matrix size
        :type new_size: set
        :return: matrix with widgets size
        :rtype: binary matrix
        """
        result = list()
        self._list_walker(
            array=matrix[::-1],
            size=new_size[0],
            func=partial(
                self._list_walker, size=new_size[1], func=result.append))
        return reshape(result, new_size)

    def _list_walker(self, array=None, size=None, func=None):
        """Resize array

        :param array: array to resize
        :type array: iterable or None
        :param size: new array size
        :type size: int or None
        :param func: func to call with next array's element
        :type func: function or None
        """
        ratio = Decimal(len(array)) / Decimal(size)
        factor = 0
        sub = 0
        for element in array:
            while ratio * factor - sub < 1:
                func(element)
                factor += 1
            if ratio * factor - sub >= 1:
                sub += 1
