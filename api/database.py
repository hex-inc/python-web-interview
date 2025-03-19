from pathlib import Path
import json
from typing import List, Optional
from models import Project

class ProjectDatabase:
    def __init__(self):
        data_dir = Path(__file__).parent.parent / 'src' / 'api' / 'data'
        with open(data_dir / 'projects.json', 'r') as f:
            raw_data = json.load(f)
            # Convert raw dictionaries to Project objects
            self._items = [Project(**item) for item in raw_data]
    
    def get_items(
        self,
        page_size: int = 10,
        start_after: Optional[Project] = None
    ) -> List[Project]:
        """
        Returns a page of items from the database.
        If start_after is provided, returns items after that item.
        
        Args:
            page_size: Number of items to return
            start_after: The Project object to start after, or None for first page
            
        Returns:
            List of Project objects for the requested page
        """
        if start_after is None:
            return self._items[:page_size]
            
        # Find the index of the start_after item
        start_idx = next(
            (i for i, item in enumerate(self._items) 
             if item.id == start_after.id),
            -1
        )
        
        if start_idx == -1:
            return self._items[:page_size]
            
        # Return items after the found index
        return self._items[start_idx + 1:start_idx + 1 + page_size] 