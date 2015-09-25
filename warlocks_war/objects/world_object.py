from kivy.uix.widget import Widget


class WorldObject(Widget):
    def __init__(self, *args, **kwargs):
        super(WorldObject, self).__init__(*args, **kwargs)
        self.register_event_type("on_update")

    def update(self):
        self.dispatch("on_update")

    def on_update(self):
        pass
