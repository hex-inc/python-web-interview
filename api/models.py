from dataclasses import dataclass


@dataclass
class Project:
    id: int
    title: str
    creatorId: int
