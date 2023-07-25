#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple
def index_range(page, page_size):
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple: A tuple of size two containing the start index (inclusive) and
               the end index (exclusive) corresponding to the range of indexes
               to return in a list for those particular pagination parameters.
    """
    # Convert the page number to 0-indexed, and calculate the start and end indexes
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index