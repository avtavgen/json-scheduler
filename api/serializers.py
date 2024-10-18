from dataclasses import dataclass
from typing import List

from rest_framework import serializers

from api.models import ScheduleName


class ScheduleNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScheduleName
        fields = ["name"]


@dataclass
class Schedule:
    start: str
    end: str
    ids: List[str] = None
    camera_ids: List[str] = None


@dataclass
class DayOfWeek:
    name: List[Schedule]


@dataclass
class Response:
    schedule: List[DayOfWeek]
