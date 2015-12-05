from kivy.vector import Vector
from numpy import array

from warlocks_war.objects.behaviour_mixins.bitmap import Bitmap
from warlocks_war.objects.behaviour_mixins.collidable import Collidable


class BitmapCollidable(Bitmap, Collidable):
    def collide_widget(self, widget):
        if super(Bitmap, self).collide_widget(widget):
            return Collidable.get_intersection(self, widget) is not None
        return False

    def collide_point(self, x, y):
        if super(Bitmap, self).collide_point(x, y):
            relative_x, relative_y = self._get_relative_coords_by_absolute(x, y)
            if 0 <= relative_x < self.size[0] and 0 <= relative_y < self.size[1]:
                return self.bitmap[relative_y, relative_x]
        return False

    def get_collide_check_pixels(self):
        check_pixels = []
        for x in range(self.size[0] + 1):
            for y in range(self.size[1] + 1):
                check_pixels.append((x, y))
        return check_pixels

