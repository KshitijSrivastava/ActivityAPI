from django.core.management.base import BaseCommand, CommandError

from activity.models import User, Activity
from activity.serializers import ActivityUserSerializer

class Command(BaseCommand):
    help = 'Helps to populate the DB with some dummy data'

    def handle(self, *args, **kwargs):
        data_array = [{
            "real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
            "start_datetime": "Feb 1 2020  1:33PM",
            "end_datetime": "Feb 1 2020 1:54PM"
        },{
            "real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
            "start_datetime": "Mar 1 2020  11:11AM",
            "end_datetime": "Mar 1 2020 2:00PM"
        },{
            "real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
            "start_datetime": "Mar 16 2020  5:33PM",
            "end_datetime": "Mar 16 2020 8:02PM"
        },{
            "real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
            "start_datetime": "Feb 1 2020  1:33PM",
            "end_datetime": "Feb 1 2020 1:54PM"
        },{
            "real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
            "start_datetime": "Mar 1 2020  11:11AM",
            "end_datetime": "Mar 1 2020 2:00PM"
        },{
            "real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
            "start_datetime": "Mar 16 2020  5:33PM",
            "end_datetime": "Mar 16 2020 8:02PM"
        }]

        for data in data_array:
            serializer = ActivityUserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()

        self.stdout.write(self.style.SUCCESS('Done populating DB with dummy data'))
        
