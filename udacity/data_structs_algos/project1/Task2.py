"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv

max_key = ''
max_seconds = 0
with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming_number = call[0]
        seconds = int(call[3])
        if seconds > max_seconds:
            max_seconds = seconds
            max_key = incoming_number

print(f"{max_key} spent the longest time, {max_seconds} seconds on the phone during September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

