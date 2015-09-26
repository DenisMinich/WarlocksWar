from numpy import ones


class RectangleShape:
    @staticmethod
    def get_matrix(x, y):
        return ones([y, x], dtype=bool)
