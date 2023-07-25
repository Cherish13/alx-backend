#!/usr/bin/env python3
"""Basic caching module.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache class inherits from BaseCaching and is a caching system.
    """

    def put(self, key, item):
        """Assign the item value for the key key in the cache_data dictionary.

        Args:
            key: The key to store the item in the cache_data dictionary.
            item: The value to be stored in the cache_data dictionary.

        Note:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve the value associated with the given key from cache_data.

        Args:
            key: The key whose value needs to be retrieved from cache_data.

        Returns:
            The value associated with the key if found in cache_data, else None.

        Note:
            If key is None or the key doesn't exist in cache_data, returns None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None