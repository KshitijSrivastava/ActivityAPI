from django.db import models
from timezone_field import TimeZoneField
import json
import datetime

# Create your models here.

class User(models.Model):
    real_name = models.CharField(max_length=50)
    tz = TimeZoneField(default='Asia/Kolkata')

    def __str__(self):
        return self.real_name

    def to_json(self):
        return {
            "user-id": self.id,
            "real_name": self.real_name,
            "tz": str(self.tz)
        }

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def to_json(self):
        return {
            "user-id": self.user.id,
            "real_name": self.user.real_name,
            "tz": str(self.user.tz) ,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime
        }

    def to_json_shortened(self):
        return {
            "start_datetime": self.start_datetime.strftime('%b %d %Y %I:%M%p'),
            "end_datetime": self.end_datetime.strftime('%b %d %Y %I:%M%p')
        }
