from collections import defaultdict
from types import MethodType


class Collector:

    _collections = defaultdict(list)

    @staticmethod
    def get_collections():
        return Collector._collections

    @staticmethod
    def get_collection(collection_name):
        return Collector._collections[collection_name]

    @staticmethod
    def add_to_collection(instance, collection_name):
        Collector._collections[collection_name].append(instance)
        instance.delete = MethodType(Collector.delete_from_collections, instance)
        instance.add_to_collection = MethodType(Collector.add_to_collection, instance)

    @staticmethod
    def assign_collection(collection_name, collection):
        collection.extend(Collector.get_collection(collection_name))
        Collector._collections[collection_name] = collection

    @staticmethod
    def delete_from_collections(instance):
        for collection in Collector._collections.values():
            if instance in collection:
                collection.remove(instance)
