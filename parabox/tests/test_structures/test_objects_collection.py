import mock
import unittest

from parabox.base_object import BaseObject
from parabox.structures import ObjectsCollection


class TestObjectsCollection(unittest.TestCase):
    def setUp(self):
        self.parent = BaseObject()
        self.first = BaseObject()
        self.second = BaseObject()
        self.collection = ObjectsCollection(
            objects=[self.first, self.second],
            parent_widget=self.parent)

    def test_ierarchy(self):
        self.assertIn(self.first, self.parent.children)
        self.assertIn(self.second, self.parent.children)

    def test_add_remove_from_collection(self):
        fourth = BaseObject()
        self.collection.append(fourth)
        self.assertIn(fourth, self.parent.children)
        self.collection.remove(self.second)
        self.assertNotIn(self.second, self.parent.children)
        self.assertIn(fourth, self.parent.children)
        self.collection.clear()
        self.assertNotIn(fourth, self.parent.children)

    def test_update_collection(self):
        first_mock = mock.Mock()
        self.first.bind(on_update=first_mock.some_method)
        second_mock = mock.Mock()
        self.second.bind(on_update=second_mock.some_method)
        self.parent.update()
        self.assertEqual(first_mock.some_method.call_count, 1)
        self.assertEqual(second_mock.some_method.call_count, 1)
