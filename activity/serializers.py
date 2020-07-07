from rest_framework import serializers
from datetime import datetime
from activity.models import Activity, User

class ActivityUserSerializer(serializers.Serializer):
    start_datetime = serializers.CharField()
    end_datetime = serializers.CharField()
    real_name = serializers.CharField()
    tz = serializers.CharField()

    def save(self):
        user = User.objects.get_or_create(
            real_name= self.validated_data.pop('real_name'), 
            defaults={'tz': self.validated_data.pop('tz')} 
            )[0]

        from_datetime = datetime.strptime( 
            self.validated_data.pop('start_datetime'), '%b %d %Y %I:%M%p')
        to_datetime =  datetime.strptime( 
            self.validated_data.pop('end_datetime'), '%b %d %Y %I:%M%p')

        activity = Activity.objects.get_or_create(
            user=user,
            start_datetime=from_datetime,
            end_datetime=to_datetime
        )[0]

        return activity.to_json()