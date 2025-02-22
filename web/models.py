from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class TimeSlotTag(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TimeSlot(models.Model):
    title = models.CharField(max_length=256)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    is_realtime = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TimeSlotTag)
    image = models.ImageField(upload_to='time_slots/', null=True, blank=True)


class Holiday(models.Model):
    date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)



