import datetime

# Get the current time
current_time = datetime.datetime.now().time()

# Format the time to 24-hour format
formatted_time = current_time.strftime("%H:%M:%S")

print("The current time in 24-hour format is:", formatted_time)
