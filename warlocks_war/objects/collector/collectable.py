from warlocks_war.objects.collector.collector import Collector


class Collectable:

    def add_to_collections(self, collections_names):
        for collection in Collector.get_collections(collections_names):
            collection.append(self)

    def delete_from_collections(self, collections_names=None):
        for collection in Collector.get_collections(collections_names):
            if self in collection:
                collection.remove(self)
