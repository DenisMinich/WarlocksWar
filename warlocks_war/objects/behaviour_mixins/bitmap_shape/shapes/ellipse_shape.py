from kivy.vector import Vector
from numpy import array


class EllipseShape:
    @staticmethod
    def get_matrix(width, height):
        factor = width / height
        radius = height / 2
        return array([
            [
                Vector(x / factor - radius, y - radius).length() < radius for x in range(width)
            ] for y in range(height)
        ], dtype=bool)
