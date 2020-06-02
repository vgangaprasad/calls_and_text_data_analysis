"""
This program finds out Which telephone number spent the longest time on the phone
during the period? It includes time spent answering a call also. 

Finally reports the telephone number with the longest time on the phone during the period.
"""

import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Dictionary to store the phone numbers and the time spent. Every time we find the telephone number
# the time spent will added to the existing time.
phone_numbers = {}

# Variable to hold the longest_time
longest_time = 0

for call in calls:

    # First adding/updating all the calling numbers to the dictionary and adding the time spent
    if call[0] not in phone_numbers:
        phone_numbers[call[0]] = int(call[3])
    else:
        phone_numbers[call[0]] += int(call[3])
    
    # Finding out the longest_time and storing the telephone number
    if phone_numbers[call[0]] > longest_time:
        longest_time = phone_numbers[call[0]]
        tel_no = call[0]
    
    # Second adding/updating the call receiving numbers to the dictionary and adding the 
    # time spent.
    if call[1] not in phone_numbers:
        phone_numbers[call[1]] = int(call[3])
    else:
        phone_numbers[call[1]] += int(call[3])
    
    # Finding out the longest_time and storing the telephone number
    if phone_numbers[call[1]] > longest_time:
        longest_time = phone_numbers[call[1]]
        tel_no = call[1]
    
print(f"{tel_no} spent the longest time, {longest_time} seconds, on the phone during \
September 2016.")

