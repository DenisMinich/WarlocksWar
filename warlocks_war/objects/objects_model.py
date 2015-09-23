class ObjectsModel(list):
    def __init__(self, *args, parent_widget=None):
        super(ObjectsModel, self).__init__(args)
        self.parent_widget = parent_widget
        for new_object in args:
            self.parent_widget.add_widget(new_object)

    def append(self, new_object):
        super(ObjectsModel, self).append(new_object)
        self.parent_widget.add_widget(new_object)

    def insert(self, index, new_object):
        super(ObjectsModel, self).insert(index, new_object)
        self.parent_widget.add_widget(new_object)

    def pop(self, index):
        result = super(ObjectsModel, self).pop(index)
        self.parent_widget.remove_widget(result)
        return result

    def remove(self, object_to_remove):
        super(ObjectsModel, self).remove(object_to_remove)
        self.parent_widget.remove_widget(object_to_remove)

    def clear(self):
        super(ObjectsModel, self).append()
        self.parent_widget.clear()

    def extend(self, iterable):
        super(ObjectsModel, self).extend(iterable)
        for new_object in iterable:
            self.parent_widget.add_widget(new_object)
