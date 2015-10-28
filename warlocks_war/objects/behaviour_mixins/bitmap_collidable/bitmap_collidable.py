from kivy.vector import Vector
from numpy import array

from warlocks_war.objects.behaviour_mixins.bitmap import Bitmap
from warlocks_war.objects.behaviour_mixins.collidable import Collidable


class BitmapCollidable(Bitmap, Collidable):
    def collide_widget(self, widget):
        if super(Bitmap, self).collide_widget(widget):
            return bool(self._get_widgets_collide_point(widget))
        return False

    def collide_point(self, x, y):
        if super(Bitmap, self).collide_point(x, y):
            relative_x, relative_y = self._get_relative_coords_by_absolute(x, y)
            bitmap_x, bitmap_y = self._get_bitmap_coords_by_relative(relative_x, relative_y)
            if 0 <= bitmap_x < self.bitmap.shape[1] and 0 <= bitmap_y < self.bitmap.shape[0]:
                return self.bitmap[bitmap_y, bitmap_x]
        return False

