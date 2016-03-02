class ObjectsCollection:
    """Widgets collection with automatic parent/child assigning
    """

    _objects = set()

    _assigned = None

    def __init__(self, objects, parent_widget):
        """ObjectsCollection constructor

        :param objects: collection to assign
        :type objects: iterable
        :param parent_widget: parent widget for objects in collection
        :type parent_widget: Widget
        """
        self._assigned = objects
        self.parent_widget = parent_widget
        self.parent_widget.bind(on_update=self.update)
        self._update_collection_state()

    def __getattr__(self, name):
        """Call inner list attribute if not found in wrapper class

        :param name: name of attribute
        :type name: string
        :returns: getattr result of inner collection
        :rtype: attr
        """
        return getattr(self._assigned, name)

    def update(self, *args, **kwargs):
        """Call update method for all objects in collection"""
        self._update_collection_state()
        for world_object in self._objects:
            world_object.update(*args, **kwargs)

    def assign_collection(self, new_collection):
        """Change assigned collection

        :param new_collection: new collection to listen
        :type new_collection: iterable
        """
        self._assigned = new_collection
        self._update_collection_state()

    def _update_collection_state(self):
        """Changed inner collection depends on assigned collection
        """
        assigned_as_set = set(self._assigned)
        for new_object in assigned_as_set - self._objects:
            if new_object.parent:
                new_object.parent.remove_widget(new_object)
            self.parent_widget.add_widget(new_object)
        for object_to_delete in self._objects - assigned_as_set:
            if object_to_delete.parent:
                self.parent_widget.remove_widget(object_to_delete)
        self._objects = assigned_as_set
