from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget


class Movable(Widget):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self, acceleration=0):
        self.x += self.velocity_x
        if self.x < 0:
            self.x = 0
            self.move_stop_x()
        self.y += self.velocity_y
        if self.y < 0:
            self.y = 0
            self.move_stop()

    def move_stop_x(self):
        self.velocity_x = self.acceleration_x = 0

    def move_stop_y(self):
        self.velocity_y = self.acceleration_y = 0

    def move_stop(self):
        self.move_stop_x()
        self.move_stop_y()
