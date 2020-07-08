# ActivityAPI

## Backend Python I Assignment | FullThrottle Labs


Design and implement a Django application with User and ActivityPeriod models, write a custom management command to populate the database with some dummy data, and design an API to serve that data in the json format given below.

```
{
	"ok": true,
	"members": [{
			"id": "W012A3CDE",
			"real_name": "Egon Spengler",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "W07QCRPA4",
			"real_name": "Glinda Southgood",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}
```

# Documentation

# Creates a User and Activity (with time duration)

Creates and saves in database, the details of the user along with his activity datetime. It also creates a user if user not present in database.

**URL** : `/activity/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Data example** All fields must be sent.

* real_name: Name of the user or person
* tz: Timezone in which the person resides
* start_datetime: Start datetime of the activity
* end_datetime: End datetime of the activity

```json
{
    "real_name": "Egon Spengler",
    "tz": "America/Los_Angeles",
    "start_datetime": "Feb 01 2020 01:33PM",
    "end_datetime": "Feb 01 2020 01:54PM"
}
```

## Success Response

**Code** : `201 Created`

**Content examples**

For a User with real_name Egon Spengler and timezone of America/Los_Angeles, it has the following start_datetime and end_datetime.

```json
{
    "id": 1,
    "real_name": "Egon Spengler",
    "tz": "America/Los_Angeles",
    "start_datetime": "2020-03-01T11:11:00Z",
    "end_datetime": "2020-03-01T14:00:00Z"
}
```

