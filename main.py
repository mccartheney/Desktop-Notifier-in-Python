from getData import GetData
from notificationCreator import notificationCreator

# Time (in minutes) between notifications
time = 10

# Get all data in Json
data = GetData().getJson()

# Create Notifications spaced by time
notificationCreator().notificationFromArray(data, data)