from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget


class Movable(Widget):
    velocity_y = NumericProperty(0)
    velocity_x = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def __init__(self, *args, **kwargs):
        super(Movable, self).__init__(*args, **kwargs)
        self.in_move = False
        self.register_event_type('on_move')
        self.register_event_type('on_move_x')
        self.register_event_type('on_move_y')
        self.register_event_type('on_stop')
        self.register_event_type('on_stop_x')
        self.register_event_type('on_stop_y')

    def move(self):
        # temp code to keep object in window's borders
        # shoud be moved to collision module... later...
        if self.x < 0:
            self.velocity_x = 0
        if self.y < 0:
            self.velocity_y = self.velocity_x = 0

        self.x += self.velocity_x
        if self.velocity_x:
            self.dispatch("on_move_x")
        self.y += self.velocity_y
        if self.velocity_y:
            self.dispatch("on_move_y")
        if self.velocity_y or self.velocity_x:
            self.dispatch("on_move")

    def move_stop_x(self):
        self.velocity_x = 0

    def move_stop_y(self):
        self.velocity_y = 0

    def move_stop(self):
        self.move_stop_x()
        self.move_stop_y()

    def on_velocity_x(self, instance, value):
        if not value and self.in_move:
            self.dispatch("on_stop_x")
            if not self.velocity_y:
                self.dispatch("on_stop")

    def on_velocity_y(self, instance, value):
        if not value and self.in_move:
            self.dispatch("on_stop_y")
            if not self.velocity_x:
                self.dispatch("on_stop")

    def on_move(self):
        self.in_move = True

    def on_move_x(self):
        pass

    def on_move_y(self):
        pass

    def on_stop(self):
        self.in_move = False

    def on_stop_x(self):
        pass

    def on_stop_y(self):
        pass
