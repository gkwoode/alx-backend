#!/usr/bin/env python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import defaultdict


class LFUCache(BaseCaching):
    """ LFUCache class defines a caching system using the LFU algorithm.

    It inherits from BaseCaching and implements the put and get methods
    to add and retrieve items from the cache, respectively.
    """

    def __init__(self):
        """ Initialize the LFUCache.

        Calls the parent class's init to initialize
        the cache_data dictionary.
        """
        super().__init__()
        # To store the frequency of each key
        self.frequency = defaultdict(int)
        # To store keys by their frequencies
        self.frequency_list = defaultdict(list)
        # To track the minimum frequency in the cache
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item in the cache.

        Args:
            key (any): The key for the item to be cached.
            item (any): The item to be cached.

        Note:
            If key or item is None, this method does not do anything.
            If the number of items in self.cache_data is higher
            than BaseCaching.MAX_ITEMS, it discards the least frequency
            used item from the cache using the LFU algorithm.
            If there is more than one item to discard, it uses the LRU
            algorithm to discard only the least recently
            used among those items.
            It prints DISCARD: with the key discarded and
            follows with a new line.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

            # Update the frequency dictionary
            self.frequency[key] += 1

            # Update the frequency list
            frequency = self.frequency[key]
            self.frequency_list[frequency].append(key)

            # Check if the cache has exceeded the max items limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                while not self.frequency_list[self.min_frequency]:
                    # If the minimum frequency is not found,
                    # increment to the next one
                    self.min_frequency += 1
                # Get the least frequency used item (LFU algorithm)
                lfu_key = self.frequency_list[self.min_frequency].pop(0)

                # If there are more than one item to discard,
                # use LRU algorithm
                if not self.frequency_list[self.min_frequency]:
                    del self.frequency_list[self.min_frequency]
                self.frequency.pop(lfu_key)

                print("DISCARD:", lfu_key)

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
            # Increment the frequency of the accessed key
            self.frequency[key] += 1

            # Move the key to the correct frequency list
            current_frequency = self.frequency[key]
            self.frequency_list[current_frequency].append(key)

            # Remove the key from its previous frequency list
            self.frequency_list[self.frequency[key] - 1].remove(key)

            # If the previous frequency list is empty,
            # update the min_frequency
            if not self.frequency_list[self.frequency[key] - 1]:
                self.min_frequency += 1

            return self.cache_data[key]

        return None


if __name__ == "__main__":
    # Add any test cases or usage examples here
    pass
