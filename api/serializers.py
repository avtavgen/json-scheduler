from dataclasses import dataclass
from typing import List


@dataclass
class Schedule:
    start: str
    stop: str
    ids: List[str] = None
    camera_ids: List[str] = None


@dataclass
class Week:
    monday: List[Schedule]
    tuesday: List[Schedule]
    wednesday: List[Schedule]
    thursday: List[Schedule]
    friday: List[Schedule]
    saturday: List[Schedule]
    sunday: List[Schedule]


@dataclass
class Root:
    schedule: Schedule
