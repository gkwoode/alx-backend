#!/usr/bin/env python3
""" LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache class defines a caching system using the LRU algorithm.

    It inherits from BaseCaching and implements the put and get methods
    to add and retrieve items from the cache, respectively.
    """

    def __init__(self):
        """ Initialize the LRUCache.

        Calls the parent class's init to initialize
        the cache_data dictionary.
        """
        super().__init__()
        self.access_order = []  # To maintain the access order of keys

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (any): The key for the item to be cached.
            item (any): The item to be cached.

        Note:
            If key or item is None, this method does not do anything.
            If the number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS, it discards the least recently
            used item from the cache using the LRU algorithm.
            It prints DISCARD: with the key discarded
            and follows with a new line.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if key in self.access_order:
                # Remove the key from its current position
                # in the access order
                self.access_order.remove(key)

            # Append the key at the end of the access
            # order list to indicate it was recently used
            self.access_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the least recently used item (LRU algorithm)
                lru_key = self.access_order.pop(0)
                print("DISCARD:", lru_key)
                del self.cache_data[lru_key]

    def get(self, key):
        """ Get an item by key.

        Args:
            key (any): The key to retrieve the item from the cache.

        Returns:
            any: The cached item corresponding to the provided key.
                 If key is None or does not exist in self.cache_data,
                 returns None.
        """
        if key in self.cache_data:
            # Move the key to the end of the access order list
            # to indicate it was recently used
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None


if __name__ == "__main__":
    # Add any test cases or usage examples here
    pass
