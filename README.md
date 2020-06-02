# Calls and Text Data Analysis


## Introduction & Purpose

Got some data about the calls and texts exchanged for a month and decided to use Python to analyze and share about the texts and calls contained in the dataset. And also, added a analysis.txt file with the run time analysis of the scripts.


## About the data

The text and call data are present in csv files.

The text data (text.csv) has the following columns:    

sending telephone number (string),    
receiving telephone number (string),    
timestamp of text message (string).

The call data (call.csv) has the following columns:    

calling telephone number (string),    
receiving telephone number (string),    
start timestamp of telephone call (string),    
duration of telephone call in seconds (string)

All telephone numbers are 10 or 11 numerical digits long. Each telephone number starts with a code indicating the location and/or type of the telephone number. There are three different kinds of telephone numbers, each with a different format:   

Fixed lines start with an area code enclosed in brackets. The area codes vary in length but always begin with 0. Example: "(022)40840621".    
Mobile numbers have no parentheses, but have a space in the middle of the number to help readability. The mobile code of a mobile number is its first four digits and they always start with 7, 8 or 9. Example: "93412 66159".    
Telemarketers' numbers have no parentheses or space, but start with the code 140. Example: "1402316533".    



## Task0
1. create_tables.py and sql_queries.py are used to creates tables, select, insert rows within a Postgresql database named 'sparkifydb'
    
2. The database has been created using a 'star schema' with fact and dimension tables, to allow analysis of user's 'song plays' on the app
    
3. Two collections of JSON log files are the data sources for the database: 'song data' and 'log_data'


