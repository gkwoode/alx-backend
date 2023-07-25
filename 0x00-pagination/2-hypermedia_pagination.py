#!/usr/bin/env python3

"""
Pagination Utility - index_range

This module contains a utility function for calculating the start and end
indexes for pagination given the page number and page size.

Page numbers are 1-indexed, i.e. the first page is page 1.

Example:
    start_idx, end_idx = index_range(3, 10)
    # Returns (20, 29) for the third page with a page size of 10.

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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """
        Retrieve a hyperlinked page of data from the dataset.

        Args:
            page (int, optional): The page number (1-indexed). Default is 1.
            page_size (int, optional): The number of items per page. Default is 10.

        Returns:
            dict: A dictionary containing hyperlinked data information.

        Raises:
            ValueError: If page or page_size is less than or equal to 0.
        """
        if not isinstance(page, int) or not isinstance(page_size, int) or page <= 0 or page_size <= 0:
            raise ValueError("Both page and page_size must be positive integers.")

        dataset_page = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(dataset_page),
            'page': page,
            'data': dataset_page,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }


if __name__ == "__main__":
    server = Server()

    # Example usage:
    page_number = 3
    items_per_page = 10
    hyper_data = server.get_hyper(page=page_number, page_size=items_per_page)
    print(hyper_data)
