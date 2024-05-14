# Constants for time valculations
SECONDS_IN_A_MINUTE = 60
SECONDS_IN_AN_HOUR = 3600
SECONDS_IN_A_DAY = 86400

total_seconds = int(input("Enter the number of seconds: "))
# 105310 -> 1 days, 5 hours, 15 minutes , 10 seconds

#calculate the number of days
days = total_seconds // SECONDS_IN_A_DAY
seconds_remaining = total_seconds % SECONDS_IN_A_DAY

# calculate the number of hours
hours = seconds_remaining // SECONDS_IN_AN_HOUR
seconds_remaining %= SECONDS_IN_AN_HOUR

# calculate the number of minutes
minutes = seconds_remaining // SECONDS_IN_A_MINUTE
seconds_remaining %= SECONDS_IN_A_MINUTE

seconds = seconds_remaining

print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")