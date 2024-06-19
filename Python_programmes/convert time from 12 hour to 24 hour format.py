from datetime import datetime

def convert24(time):
	# Parse the time string into a datetime object
	t = datetime.strptime(time, '%I:%M:%S %p')
	# Format the datetime object into a 24-hour time string
	return t.strftime('%H:%M:%S')

print(convert24('11:21:30 PM')) # Output: '23:21:30'
print(convert24('12:12:20 AM')) # Output: '00:12:20'

# --------------------------------------------


import re

def convert_to_24hour(time_str):
	hour, minute, second, am_pm = re.findall('\d+|\w+', time_str)
	hour = int(hour)
	if am_pm == 'PM' and hour != 12:
		hour += 12
	elif am_pm == 'AM' and hour == 12:
		hour = 0
	return f'{hour:02d}:{minute}:{second}'
print(convert_to_24hour('11:21:30 PM'))
print(convert_to_24hour('12:12:20 AM'))
