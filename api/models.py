from dataclasses import dataclass
from typing import Optional

@dataclass
class Project:
    id: int
    title: str
    creatorId: int