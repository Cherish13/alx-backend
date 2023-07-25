#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination
"""
import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    # ... (rest of the class implementation)

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Get hypermedia pagination information for a specific index.

        Args:
            index (int, optional): The start index of the return page. Defaults to None.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing hypermedia pagination information.
        """
        assert isinstance(index, int) and index >= 0, "Index must be a non-negative integer."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)

        # Check if index is out of range
        if index >= total_items:
            return {}

        # Calculate the next index to query with
        next_index = index + page_size

        # Handle cases where certain rows may have been removed between queries
        while next_index < total_items and next_index not in indexed_dataset:
            next_index += 1

        # Get the actual data page for the current index and page size
        data = [indexed_dataset[i] for i in range(index, next_index) if i in indexed_dataset]

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index if next_index < total_items else None
        }