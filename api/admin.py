from django.contrib import admin

from api.models import DayOfWeek, Schedule, Ids, ScheduleName


admin.site.register(ScheduleName)
admin.site.register(DayOfWeek)
admin.site.register(Schedule)
admin.site.register(Ids)
