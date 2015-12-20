from parabox.behaviour.bitmap import Bitmap
from parabox.behaviour.collidable import Collidable


class BitmapCollidable(Bitmap, Collidable):
    """Mix Bitmap and Collidable behaviour"""

    def collide_widget(self, widget):
        """Check if collide another widget

        :param widget: widget to check collission
        :type widget: kivy.uix.widget.Widget
        :returns: collide result
        :rtype: bool
        """
        if super(Bitmap, self).collide_widget(widget):
            return Collidable.get_intersection(self, widget) is not None
        return False

    def collide_point(self, x_coord, y_coord):
        """Check if widget collide point

        :param x_coord: x coord of point to check
        :type y_coord: y coord of point to check
        :returns: collide result
        :rtype: bool
        """
        if super(Bitmap, self).collide_point(x_coord, y_coord):
            relative_x, relative_y = self._get_relative_coords_by_absolute(
                x_coord, y_coord)
            if (0 <= relative_x < self.size[0] and
                    0 <= relative_y < self.size[1]):
                return self.bitmap[relative_y, relative_x]
        return False

    def get_collide_check_pixels(self):
        """Get points to use for checking collission

        :returns: points for check collission
        :rtype: array of sets
        """
        check_pixels = []
        for x in range(self.size[0] + 1):
            for y in range(self.size[1] + 1):
                check_pixels.append((x, y))
        return check_pixels
