#!/usr/bin/env python3

"""
Pagination Utility - index_range
"""

import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indexes for pagination.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        tuple[int, int]: A tuple containing the start index and end index
                         for the given page.

    Raises:
        ValueError: If the page or page_size is less than or equal to 0.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    return start_index, end_index


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieve a page of data from the dataset.

        Args:
            page (int, optional): The page number (1-indexed). Default is 1.
            page_size (int, optional): The number of items per page. Default is 10.

        Returns:
            List[List]: A list of rows corresponding to the requested page.

        Raises:
            ValueError: If page or page_size is less than or equal to 0.
        """
        if not isinstance(page, int) or not isinstance(page_size, int) or page <= 0 or page_size <= 0:
            raise ValueError("Both page and page_size must be positive integers.")

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx + 1]


if __name__ == "__main__":
    server = Server()

    # Example usage:
    page_number = 3
    items_per_page = 10
    page_data = server.get_page(page=page_number, page_size=items_per_page)
    print(page_data)
