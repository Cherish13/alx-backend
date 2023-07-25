#!/usr/bin/env python3
"""Hypermedia pagination sample.
"""
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> tuple:
        """Calculate the start and end indexes for pagination.

        Args:
            page (int): The current page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            tuple: A tuple of size two containing the start index (inclusive) and
                   the end index (exclusive) corresponding to the range of indexes
                   to return in a list for those particular pagination parameters.
        """
        # Calculate the start and end indexes
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the specified page of the dataset.

        Args:
            page (int, optional): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            List[List]: The list of rows corresponding to the specified page.
        """
        assert isinstance(page, int) and page > 0, "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, "Page size must be an integer greater than 0."

        dataset = self.dataset()
        start_index, end_index = self.index_range(page, page_size)

        # Check if the specified page is out of range for the dataset
        if start_index >= len(dataset):
            return []

        # Return the page of data
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hypermedia pagination information.

        Args:
            page (int, optional): The page number to retrieve (1-indexed). Defaults to 1.
            page_size (int, optional): The number of items per page. Defaults to 10.

        Returns:
            dict: A dictionary containing hypermedia pagination information.
        """
        page_data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }