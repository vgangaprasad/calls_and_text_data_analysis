"""
This program finds out how many different telephone numbers are there in the records? 
And finally prints the unique telephone numbers in the records.
"""
import csv

# Dictionary to store the unique numbers
phone_numbers = {}

with open('texts.csv', 'r') as f:
    i = 0
    reader = csv.reader(f)
    texts = list(reader)


with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Process the numbers from the texts file and adds the unique numbers to the dictionary
for text in texts:
    if text[0] not in phone_numbers:
        phone_numbers[text[0]] = True
    if text[1] not in phone_numbers:
        phone_numbers[text[1]] = True

# Process the numbers from the calls file and adds the unique numbers to the dictionary
for call in calls:
    if call[0] not in phone_numbers:
        phone_numbers[call[0]] = True
    if call[1] not in phone_numbers:
        phone_numbers[call[1]] = True

# Prints the total number of unique numbers from both texts and calls data.
print(f'There are {len(phone_numbers)} different telephone numbers in the records.')


