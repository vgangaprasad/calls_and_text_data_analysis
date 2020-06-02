import csv


def calledToAreaCode(calls):
  """
  This function reads the calls data and gathers all area codes and mobile prefixes
  called by people in Bangalore (numbers starting with (080))
  """
  # dictionary to store the list of Area codes, mobile prefixes
  prefix = []

  # variable to store the percentage of Calls
  percentCalls = 0.0
  
  # Variable to store total number of calls made.
  numOfCalls = 0

  # Variable to store total number of Landline calls made.
  numOfLandLine = 0


  # For each call, gather the prefix and the area code of the numbers that were called from
  # Bangalore (Numbers starting with (080))
  for call in calls:
    if call[0][0:5] == '(080)':
      numOfCalls += 1
      
      if call[1][0] == '(':
        i = 1
        # temp variable to hold the data between ( and )
        temp_pre =''
        while call[1][i] != ')':
          temp_pre += call[1][i]
          i += 1
        
        if temp_pre == '080':
          numOfLandLine += 1
        
        if temp_pre not in prefix:
          prefix.append(temp_pre)
      
      elif call[1][0] in ('7', '8', '9'):
        if call[1][0:4] not in prefix:
          prefix.append(call[1][0:4])
      
      elif call[1][0:3] == '140':
        if '140' not in prefix:
          prefix.append('140')

  
  print("The numbers called by people in Bangalore have codes:")
  for area in prefix:
    print(area)
  
  # Calcualte the percentage Calls
  percentCalls = round(float((numOfLandLine/numOfCalls)*100),2)
  
  print(f"{percentCalls} percent of calls from fixed lines in Bangalore are calls \
to other fixed lines in Bangalore.")
  return


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

calledToAreaCode(calls)



