class ObjectsCollection(list):
    """Widgets collection with automatic parent/child assigning"""

    def __init__(self, objects, parent_widget):
        """ObjectsCollection constructor

        :param objects: objects to add
        :type objects: iterable
        :param parent_widget: parent widget for objects in collection
        :type parent_widget: Widget
        """
        super(ObjectsCollection, self).__init__(objects)
        self.parent_widget = parent_widget
        self.parent_widget.bind(on_update=self.update)
        for new_object in objects:
            self.parent_widget.add_widget(new_object)

    def append(self, new_object):
        """Append object to collection

        :param new_object: object to append
        :type new_object: any
        """
        super(ObjectsCollection, self).append(new_object)
        self.parent_widget.add_widget(new_object)

    def insert(self, index, new_object):
        """Insert object to collection

        :param new_object: object to insert
        :type new_object: any
        :param index: insert position
        :type index: int
        """
        super(ObjectsCollection, self).insert(index, new_object)
        self.parent_widget.add_widget(new_object)

    def pop(self, index):
        """Pop object from collection

        :param index: pop position
        :type index: int
        """
        result = super(ObjectsCollection, self).pop(index)
        self.parent_widget.remove_widget(result)
        return result

    def remove(self, object_to_remove):
        """Remove object from collection

        :param object_to_remove: object to remove
        :type object_to_remove: any
        """
        super(ObjectsCollection, self).remove(object_to_remove)
        self.parent_widget.remove_widget(object_to_remove)

    def clear(self):
        """Clear collection"""
        for widget_to_delete in self:
            self.parent_widget.remove_widget(widget_to_delete)
        super(ObjectsCollection, self).clear()

    def extend(self, iterable):
        """Extend collection with iterable

        :param iterable: objects to extend collection
        :type iterable: iterable
        """
        super(ObjectsCollection, self).extend(iterable)
        for new_object in iterable:
            self.parent_widget.add_widget(new_object)

    def update(self, *args, **kwargs):
        """Call update method for all objects in collection"""
        for world_object in self:
            world_object.update(*args, **kwargs)
