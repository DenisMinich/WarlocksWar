from collections import defaultdict

import unittest

from parabox.base_object import BaseObject
from parabox.structures import Collector


class CollectableExample(BaseObject):
    def __init__(self, *args, **kwargs):
        super(CollectableExample, self).__init__(*args, **kwargs)
        self.add_to_collections(['example_collection'])


class TestCollector(unittest.TestCase):
    def setUp(self):
        self.initial = Collector._collections
        Collector._collections = defaultdict(set)
        self.instance = CollectableExample()

    def tearDown(self):
        Collector._collections = self.initial

    def test_in_base_objects_by_default(self):
        self.assertIn(self.instance, Collector.get_collection(
            'base_objects'))

    def test_add_and_delete_from_collection(self):
        self.instance.add_to_collections(['another_one_collection'])
        self.assertIn(self.instance, Collector.get_collection(
            'example_collection'))
        self.assertIn(self.instance, Collector.get_collection(
            'another_one_collection'))
        self.instance.delete_from_collections(['example_collection'])
        self.assertNotIn(self.instance, Collector.get_collection(
            'example_collection'))
        self.assertIn(self.instance, Collector.get_collection(
            'another_one_collection'))

    def test_get_collection(self):
        self.assertEqual(
            len(Collector.get_collection('new_collection')), 0)
        self.assertEqual(
            len(Collector.get_collection('example_collection')), 1)

    def test_get_collections(self):
        initial_len = len(list(Collector.get_collections()))
        self.assertEqual(
            len(list(Collector.get_collections(['foo', 'bar']))), 2)
        self.assertEqual(
            len(list(Collector.get_collections())), initial_len + 2)
