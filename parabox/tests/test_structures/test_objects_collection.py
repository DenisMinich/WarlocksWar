import mock
import unittest

from parabox.base_object import BaseObject
from parabox.structures import ObjectsCollection


class TestObjectsCollection(unittest.TestCase):
    def setUp(self):
        self.parent = BaseObject()
        self.first = BaseObject()
        self.second = BaseObject()
        self.third = BaseObject()
        self.assigned_list = [self.first, self.second]
        self.collection = ObjectsCollection(
            objects=self.assigned_list,
            parent_widget=self.parent)
        self.collection.update()

    def test_ierarchy(self):
        self.assertIn(self.first, self.parent.children)
        self.assertIn(self.second, self.parent.children)
        self.assertNotIn(self.third, self.parent.children)

    def test_update_on_list_change(self):
        self.assigned_list.append(self.third)
        self.collection.update()
        self.assertIn(self.third, self.parent.children)
        self.assigned_list.remove(self.second)
        self.collection.update()
        self.assertNotIn(self.second, self.parent.children)
        self.assertIn(self.third, self.parent.children)
        self.collection.clear()
        self.collection.update()
        self.assertNotIn(self.third, self.parent.children)

    def test_update_collection(self):
        first_mock = mock.Mock()
        self.first.bind(on_update=first_mock.some_method)
        second_mock = mock.Mock()
        self.second.bind(on_update=second_mock.some_method)
        self.parent.update()
        self.assertEqual(first_mock.some_method.call_count, 1)
        self.assertEqual(second_mock.some_method.call_count, 1)

    def test_auto_source_update(self):
        self.collection.append(self.third)
        self.assertIn(self.third, self.assigned_list)
        self.collection.remove(self.first)
        self.assertNotIn(self.first, self.assigned_list)

    def test_change_collection(self):
        another_collection = list([self.third])
        self.collection.assign_collection(another_collection)
        self.assertNotIn(self.first, self.parent.children)
        self.assertNotIn(self.second, self.parent.children)
        self.assertIn(self.third, self.parent.children)

    def test_various_collections_types(self):
        another_collection = set([self.third])
        self.collection.assign_collection(another_collection)
        self.collection.add(self.first)
        self.collection.update()
        self.assertIn(self.first, self.parent.children)
        self.assertNotIn(self.second, self.parent.children)
        self.assertIn(self.third, self.parent.children)
