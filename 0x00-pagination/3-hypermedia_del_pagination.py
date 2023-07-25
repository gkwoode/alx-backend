#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
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

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Retrieve a hyperlinked page of data from the dataset based on the index.

        Args:
            index (int, optional): The start index of the current page. Default is None.
            page_size (int, optional): The number of items per page. Default is 10.

        Returns:
            dict: A dictionary containing hyperlinked data information.

        Raises:
            ValueError: If index is out of range or not an integer.
        """
        if index is None:
            index = 0

        if not isinstance(index, int) or index < 0:
            raise ValueError("Index must be a non-negative integer.")

        dataset = self.indexed_dataset()
        total_rows = len(dataset)

        if index >= total_rows:
            return {
                'index': index,
                'next_index': None,
                'page_size': page_size,
                'data': []
            }

        next_index = min(index + page_size, total_rows)
        data = [dataset[i] for i in range(index, next_index)]

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }


if __name__ == "__main__":
    server = Server()

    # Example usage:
    start_index = 60
    items_per_page = 10
    hyper_data = server.get_hyper_index(index=start_index, page_size=items_per_page)
    print(hyper_data)
