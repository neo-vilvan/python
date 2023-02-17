import datetime

# Get the current time
now = datetime.datetime.now()

# Convert the time to the 12-hour format
time_12_hours = now.strftime("%I:%M %p")

print("Current time (12-hour format):", time_12_hours)
