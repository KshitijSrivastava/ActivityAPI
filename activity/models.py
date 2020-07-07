from django.db import models
from timezone_field import TimeZoneField
import json

# Create your models here.

class User(models.Model):
    real_name = models.CharField(max_length=50)
    tz = TimeZoneField(default='Asia/Kolkata')

    def __str__(self):
        return self.real_name

class Activity(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()

    def to_json(self):
        print(self.user.tz)
        return {
            "user-id": self.user.id,
            "realname": self.user.real_name,
            "tz": str(self.user.tz) ,
            "start_datetime": self.start_datetime,
            "end_datetime": self.end_datetime
        }
