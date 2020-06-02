"""
This program finds out the the first record of texts and the last record of calls.

And prints the following messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Prints first record of texts
print(f'First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}')
# Prints last record of texts
print(f'Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds')
