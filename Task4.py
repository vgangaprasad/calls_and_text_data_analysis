import csv

def identifyOutGoing(calls,outgoing):
    """
    This function reads the data from calls and 
    adds all the unique numbers to a dictionary
    named outgoing.
    """
    for call in calls:
        if call[0] not in outgoing:
            outgoing[call[0]] = True

def removeInComing(calls,outgoing):
    """
    This function reads the data from calls and 
    removes a telephone number if it present in 
    the outgoing dictionary with the assumption 
    that Tele Marketers don't get incoming calls.
    """
    for call in calls:
        if call[1] in outgoing:
            outgoing.pop(call[1]) 

def removeTextNumbers(texts,outgoing):
    """
    This function reads the data from texts and 
    removes a telephone number if it present in 
    the outgoing dictionary with the assumption 
    that Tele Marketers don't send text messages.
    """
    for text in texts:
        if text[0] in outgoing:
            outgoing.pop(text[0])

def printTeleMarketers(outgoing):
    """
    This function get the outgoing dictionary and
    gets and prints all the telephones numbers present 
    after removing the numbers that receives incoming 
    calls and sends text messages. 
    """
    telNumbers = list(outgoing.keys())
    telNumbers.sort()
    print("These numbers could be telemarketers: ")
    for tel in telNumbers:
        print(tel)

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Dictionary to store all the telemarketers numbers 
outgoing = {}

#calling identifyOutGoing function to add all the numbers that makes outgoing calls
identifyOutGoing(calls,outgoing)

#calling removeInComing function to remove all the numbers that receives incoming calls
removeInComing(calls,outgoing)

#calling removeTextNumbers function to remove all the numbers that sends text messages.
removeTextNumbers(texts,outgoing)

#calling printTeleMarketers function to print all the numbers that could be Tele Marketers.
printTeleMarketers(outgoing)

