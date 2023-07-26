#!/usr/bin/env python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class defines a caching system without a limit.

    It inherits from BaseCaching and implements the put and get methods
    to add and retrieve items from the cache, respectively.
    """

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (any): The key for the item to be cached.
            item (any): The item to be cached.

        Note:
            If key or item is None, this method does not do anything.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key.

        Args:
            key (any): The key to retrieve the item from the cache.

        Returns:
            any: The cached item corresponding to the provided key.
                 If key is None or does not exist in self.cache_data,
                 returns None.
        """
        return self.cache_data.get(key)


if __name__ == "__main__":
    # Add any test cases or usage examples here
    pass
