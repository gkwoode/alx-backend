#!/usr/bin/env python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache class defines a caching system using the LIFO algorithm.

    It inherits from BaseCaching and implements the put and get methods
    to add and retrieve items from the cache, respectively.
    """

    def __init__(self):
        """ Initialize the LIFOCache.

        Calls the parent class's init to initialize the cache_data dictionary.
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
            than BaseCaching.MAX_ITEMS, it discards
            the last item put in cache using the LIFO algorithm.
            It prints DISCARD: with the key discarded
            and follows with a new line.
        """

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Get the last item inserted into the cache (LIFO algorithm)
                last_item_key = list(self.cache_data.keys())[-1]
                print("DISCARD:", last_item_key)
                del self.cache_data[last_item_key]
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
