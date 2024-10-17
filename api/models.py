from django.db import models


class DayOfWeek(models.Model):
    name = models.CharField(max_length=100, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}'


class Schedule(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    weekday = models.ManyToManyField(DayOfWeek, related_name='schedules')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.start}:{self.end}'


class Ids(models.Model):
    name = models.CharField(max_length=100, blank=False)
    id_name = models.CharField(max_length=10, blank=False)
    schedule = models.ManyToManyField(Schedule, related_name='ids')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id_name}'
