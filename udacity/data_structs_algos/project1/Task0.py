"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)
    first_line = texts[0]
    incoming_number = first_line[0]
    answering_number = first_line[1]
    time = first_line[2]
    print(f"First record of texts, {incoming_number} texts {answering_number} at time {time}")

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
    last_call = calls[-1]
    incoming_number = last_call[0]
    answering_number = last_call[1]
    time = last_call[2]
    seconds = last_call[3]
    print(f"Last record of calls, {incoming_number} calls {answering_number} at time {time}, lasting {seconds} seconds")


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

