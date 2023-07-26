#!/usr/bin/env python3
""" MRUCache module
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class defines a caching system using the MRU algorithm.

    It inherits from BaseCaching and implements the put and get methods
    to add and retrieve items from the cache, respectively.
    """

    def __init__(self):
        """ Initialize the MRUCache.

        Calls the parent class's init to initialize
        the cache_data dictionary.
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (any): The key for the item to be cached.
            item (any): The item to be cached.

        Note:
            If key or item is None, this method does not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, it discards the most recently
            used item from the cache using the MRU algorithm.
            It prints DISCARD: with the key discarded and
            follows with a new line.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Get the most recently used item (MRU algorithm)
                mru_key = next(reversed(self.cache_data))
                print("DISCARD:", mru_key)
                del self.cache_data[mru_key]

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
            # Move the key to the end of the cache_data dictionary
            # to indicate it was recently used
            value = self.cache_data.pop(key)
            self.cache_data[key] = value
            return value
        return None


if __name__ == "__main__":
    # Add any test cases or usage examples here
    pass
