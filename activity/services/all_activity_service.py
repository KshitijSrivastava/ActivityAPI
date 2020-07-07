from activity.models import Activity, User


class AllActivityService():

    def get_all_activity(self):
        members = []
        for user in User.objects.all():
            user_activity = user.to_json()
            try:
                print(Activity.objects.filter(user = user))
                activity_periods = [ period.to_json_shortened() 
                for period in Activity.objects.filter(id = user.id)]
            except:
                activity_periods = []
            user_activity['activity_periods'] = activity_periods
            members.append(user_activity)
    
        return {
            "ok": True,
            "members": members
        }