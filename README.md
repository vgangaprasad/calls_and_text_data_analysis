# Calls and Text Data Analysis


## Introduction & Purpose

Got some data about the calls and texts exchanged for a month and decided to use Python to analyze and share about the texts and calls contained in the dataset. And also, added a analysis.txt file with the run time analysis of the scripts.


## About the data

The text and call data are present in csv files.

### The text data (text.csv) has the following columns:    

sending telephone number (string),    
receiving telephone number (string),    
timestamp of text message (string).

### The call data (call.csv) has the following columns:    

calling telephone number (string),    
receiving telephone number (string),    
start timestamp of telephone call (string),    
duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number.   

There are three different kinds of telephone numbers, each with a different format:   

1. Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".    

2. Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".    

3. Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".    



## Task0

The script prints out the information of first record of texts and last record of calls

## Task1

The script prints number of distinct telephone numbers in the dataset.

## Task2

The script prints the telephone number that spent the longest time on the phone and the total time in seconds they spend on phone call.

## Task3

The script prints the telephone codes called by fixed-line numbers in Bangalore and the percentage of calls from fixed lines in Bangalore that are to fixed lines in Bangalore.

## Task4

The script prints the list of numbers that could be telemarketers.


