from typing import Callable, Optional
from database import ProjectDatabase
from models import Project


def get_page(page_size: int, start_after: Optional[Project] = None):
    """
    TODO: Implement this function!

    Given pagination parameters, return a Page object containing:
    - The correct slice of items based on the pagination parameters
    - A boolean indicating if there are more results available

    Parameters:
        page_size: How many items to return per page
        start_after: Optional item to start pagination after

    Returns:
        Page object containing items and hasMoreResults attributes
    """
    db = ProjectDatabase()
    return {
        "projects": db.get_items(page_size, start_after),
        "hasMoreResults": False,  # TODO
    }


def get_page_filtered(
    page_size: int,
    filter_fn: Callable[[Project], bool],
    start_after: Optional[Project] = None,
):
    """
    TODO: Implement this function!

    Given pagination parameters and a filter function, return a Page object containing:
    - The correct slice of filtered items based on the pagination parameters
    - A boolean indicating if there are more results available

    Parameters:
        page_size: How many items to return per page
        filter_fn: Function to filter items
        start_after: Optional item to start pagination after

    Returns:
        Page object containing items and hasMoreResults attributes
    """
    return get_page(page_size, start_after)
