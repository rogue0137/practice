"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

all_phone_numbers = set()

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    for text in texts:
        incoming_number = text[0]
        answering_number = text[1]
        all_phone_numbers.add(incoming_number)
        all_phone_numbers.add(answering_number)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    for call in calls:
        incoming_number = call[0]
        answering_number = call[1]
        all_phone_numbers.add(incoming_number)
        all_phone_numbers.add(answering_number)

count = len(all_phone_numbers)
print(f"There are {count} different telephone numbers in the records.")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
