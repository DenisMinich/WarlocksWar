from collections import defaultdict


class Collectable(object):
    """Mixin for classes, which may be collected with 'Collector'"""

    def add_to_collections(self, collections_names=None):
        """Add class to specified collections

        :param collections_names: names of collections to add
        :type collections_names: iterable or None
        """
        for collection in Collector.get_collections(collections_names):
            collection.add(self)

    def delete_from_collections(self, collections_names=None):
        """Delete class from specified collections

        :param collections_names: names of collections to remove class from
        :type collections_names: iterable or None
        """
        for collection in Collector.get_collections(collections_names):
            if self in collection:
                collection.remove(self)


class Collector(object):
    """Manager class for work with collections"""

    _collections = defaultdict(set)

    @staticmethod
    def get_collection(collection_name):
        """Return single collection by name

        :param collection_name: collection's name
        :type collection_name: immutable
        :returns: specified collection
        :rtype: set
        """
        return Collector._collections[collection_name]

    @staticmethod
    def get_collections(collections_names=None):
        """Return multiple collections by names

        :param collections_names: collections' names. None for all collections
        :type collections_names: immutable
        :returns: specified collections
        :rtype: generator
        """
        if collections_names is not None:
            collections_names = collections_names
        else:
            collections_names = Collector._collections.keys()
        for collection_name in collections_names:
            yield Collector.get_collection(collection_name)
