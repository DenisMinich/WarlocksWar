from collections import defaultdict


class Collector:

    _collections = defaultdict(set)

    @staticmethod
    def get_collection(collection_name):
        return Collector._collections[collection_name]

    @staticmethod
    def get_collections(collections_names=None):
        collections_names = collections_names if collections_names is not None else Collector._collections.keys()
        for collection_name in collections_names:
            yield Collector.get_collection(collection_name)

